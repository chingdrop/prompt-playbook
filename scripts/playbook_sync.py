#!/usr/bin/env python3
"""
Playbook sync (stdlib-only)

- Treats each topic's topic_manifest.json as the single source of truth
- Auto-generates:
  - Each topic README "Prompt cards" section
  - Root TOPICS.md
  - Root README "Topics included" section

Usage:
  python scripts/playbook_sync.py --write
  python scripts/playbook_sync.py --check

Exit codes:
  0 OK
  1 In --check mode, drift found (files would change)
  2 Bad args / fatal error
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


AUTO_PROMPT_BEGIN = "<!-- BEGIN:prompt-cards (auto-generated) -->"
AUTO_PROMPT_END = "<!-- END:prompt-cards -->"

AUTO_TOPICS_BEGIN = "<!-- BEGIN:topics-index (auto-generated) -->"
AUTO_TOPICS_END = "<!-- END:topics-index -->"


@dataclass(frozen=True)
class PromptCard:
    file: str
    purpose: str


@dataclass(frozen=True)
class TopicManifest:
    topic: str
    status: str
    canonical_instructions_file: str
    canonical_knowledge_files: List[str]
    router_path: str
    prompt_cards: List[PromptCard]


def _load_manifest(path: Path) -> TopicManifest:
    data = json.loads(path.read_text(encoding="utf-8"))
    prompt_cards = [
        PromptCard(file=pc.get("file", ""), purpose=pc.get("purpose", ""))
        for pc in (data.get("prompt_cards") or [])
    ]
    return TopicManifest(
        topic=data.get("topic", path.parent.name),
        status=data.get("status", "scaffold"),
        canonical_instructions_file=data.get("canonical_instructions_file", ""),
        canonical_knowledge_files=list(data.get("canonical_knowledge_files") or []),
        router_path=data.get("router_path", ""),
        prompt_cards=prompt_cards,
    )


def _generate_prompt_cards_block(m: TopicManifest) -> str:
    lines: List[str] = [AUTO_PROMPT_BEGIN]
    for pc in m.prompt_cards:
        link = f"[`{pc.file}`](prompts/{pc.file})"
        purpose = (pc.purpose or "").strip()
        if purpose:
            lines.append(f"- {link} — {purpose}")
        else:
            lines.append(f"- {link}")
    lines.append(AUTO_PROMPT_END)
    return "\n".join(lines)


def _replace_section(text: str, heading_regex: str, new_heading: str, new_body: str) -> str | None:
    """
    Replace a level-2 section (## ...) matching heading_regex with heading+body,
    stopping at the next level-2 heading or EOF.
    """
    m = re.search(heading_regex, text, flags=re.M | re.I)
    if not m:
        return None

    start = m.start()
    line_end = text.find("\n", m.end())
    if line_end == -1:
        line_end = len(text)

    next_h2 = re.search(r"^##\s+", text[line_end + 1 :], flags=re.M)
    end = (line_end + 1 + next_h2.start()) if next_h2 else len(text)

    before = text[:start]
    after = text[end:]

    replacement = new_heading.strip() + "\n\n" + new_body.strip() + "\n\n"
    return before + replacement + after


def _upsert_prompt_cards_section(topic_dir: Path, manifest: TopicManifest, dry_run: bool) -> Tuple[bool, str]:
    """
    Ensures the topic README has an auto-generated prompt cards section.
    Returns (changed, new_text).
    """
    readme_path = topic_dir / "README.md"
    text = readme_path.read_text(encoding="utf-8")

    # Normalize older section name: "Top prompt cards" -> "Prompt cards"
    if re.search(r"^##\s+Top prompt cards\s*$", text, flags=re.M | re.I) and not re.search(
        r"^##\s+Prompt cards\s*$", text, flags=re.M | re.I
    ):
        text = re.sub(r"\(#top-prompt-cards\)", "(#prompt-cards)", text, flags=re.I)

        block = _generate_prompt_cards_block(manifest)
        updated = _replace_section(text, r"^##\s+Top prompt cards\s*$", "## Prompt cards", block)
        if updated is None:
            updated = text.rstrip() + "\n\n## Prompt cards\n\n" + block + "\n"
    elif re.search(r"^##\s+Prompt cards\s*$", text, flags=re.M | re.I):
        block = _generate_prompt_cards_block(manifest)
        updated = _replace_section(text, r"^##\s+Prompt cards\s*$", "## Prompt cards", block)
        if updated is None:
            updated = text  # should not happen
    else:
        block = _generate_prompt_cards_block(manifest)
        updated = text.rstrip() + "\n\n## Prompt cards\n\n" + block + "\n"

    changed = (updated != readme_path.read_text(encoding="utf-8"))
    if not dry_run and changed:
        readme_path.write_text(updated, encoding="utf-8")
    return changed, updated


def _topic_display_name(topic_readme: Path) -> str:
    txt = topic_readme.read_text(encoding="utf-8")
    m = re.search(r"^#\s+(.+?)\s*$", txt, flags=re.M)
    return m.group(1).strip() if m else topic_readme.parent.name


def _topic_description(topic_readme: Path) -> str:
    txt = topic_readme.read_text(encoding="utf-8")
    lines = txt.splitlines()

    # Find the H1
    i = 0
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            i = idx + 1
            break

    # Skip blanks
    while i < len(lines) and not lines[i].strip():
        i += 1

    para: List[str] = []
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            break
        if line.strip().lower().startswith("**status:**"):
            break
        if line.startswith("## "):
            break
        para.append(line.strip())
        i += 1

    desc = " ".join(para).strip()
    desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", desc)
    return desc


def _generate_topics_md(repo_root: Path, manifests: Dict[str, TopicManifest]) -> str:
    lines: List[str] = [
        "# Topics index",
        "",
        "This file is auto-generated from per-topic `topic_manifest.json` files.",
        "",
        "| Topic | Status | Prompt cards | README | Manifest | Description |",
        "|---|---:|---:|---|---|---|",
    ]

    for topic in sorted(manifests.keys()):
        m = manifests[topic]
        topic_dir = repo_root / "gpts" / topic
        readme = topic_dir / "README.md"
        title = _topic_display_name(readme)
        desc = _topic_description(readme)
        pc_count = len(m.prompt_cards)
        readme_rel = f"gpts/{topic}/README.md"
        manifest_rel = f"gpts/{topic}/topic_manifest.json"
        lines.append(
            f"| {title} | {m.status} | {pc_count} | [`{readme_rel}`]({readme_rel}) | [`{manifest_rel}`]({manifest_rel}) | {desc} |"
        )

    return "\n".join(lines) + "\n"


def _generate_root_topics_block(manifests: Dict[str, TopicManifest]) -> str:
    lines: List[str] = [AUTO_TOPICS_BEGIN]
    for topic in sorted(manifests.keys()):
        m = manifests[topic]
        lines.append(f"- [`gpts/{topic}/README.md`](gpts/{topic}/README.md) — **{m.status}**")
    lines.append(AUTO_TOPICS_END)
    return "\n".join(lines)


def _upsert_root_topics_section(repo_root: Path, manifests: Dict[str, TopicManifest], dry_run: bool) -> Tuple[bool, str]:
    readme_path = repo_root / "README.md"
    text = readme_path.read_text(encoding="utf-8")
    block = _generate_root_topics_block(manifests)

    updated = _replace_section(text, r"^##\s+Topics included\s*$", "## Topics included", block)
    if updated is None:
        updated = text.rstrip() + "\n\n## Topics included\n\n" + block + "\n"

    changed = (updated != readme_path.read_text(encoding="utf-8"))
    if not dry_run and changed:
        readme_path.write_text(updated, encoding="utf-8")
    return changed, updated


def _collect_manifests(repo_root: Path) -> Dict[str, TopicManifest]:
    manifests: Dict[str, TopicManifest] = {}
    gpts_dir = repo_root / "gpts"
    for topic_dir in gpts_dir.iterdir():
        if not topic_dir.is_dir():
            continue
        manifest_path = topic_dir / "topic_manifest.json"
        if not manifest_path.exists():
            continue
        manifests[topic_dir.name] = _load_manifest(manifest_path)
    return manifests


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Write generated files to disk")
    mode.add_argument("--check", action="store_true", help="Fail if generated files are out of date")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    dry_run = bool(args.check)

    manifests = _collect_manifests(repo_root)
    if not manifests:
        print("No topic_manifest.json files found under gpts/*/")
        return 2

    changed_any = False

    # Per-topic README updates
    for topic, m in sorted(manifests.items()):
        topic_dir = repo_root / "gpts" / topic
        changed, _ = _upsert_prompt_cards_section(topic_dir, m, dry_run=dry_run)
        if changed:
            changed_any = True
            print(f"[DRIFT] {topic_dir/'README.md'} prompt cards section is out of date")

    # Root TOPICS.md
    topics_md_path = repo_root / "TOPICS.md"
    generated_topics_md = _generate_topics_md(repo_root, manifests)
    existing_topics_md = topics_md_path.read_text(encoding="utf-8") if topics_md_path.exists() else ""
    if existing_topics_md != generated_topics_md:
        changed_any = True
        print(f"[DRIFT] {topics_md_path} is out of date")
        if not dry_run:
            topics_md_path.write_text(generated_topics_md, encoding="utf-8")

    # Root README "Topics included"
    changed, _ = _upsert_root_topics_section(repo_root, manifests, dry_run=dry_run)
    if changed:
        changed_any = True
        print(f"[DRIFT] {repo_root/'README.md'} topics section is out of date")

    if args.check and changed_any:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
