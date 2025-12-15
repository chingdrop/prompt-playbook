#!/usr/bin/env python3
"""
Playbook lint (stdlib-only)

Validates each topic against its topic_manifest.json as the single source of truth:

- status=complete requires: router + >=3 prompt cards + knowledge + canonical instructions
- router allowlist must only reference existing prompt cards listed in manifest
- prompt cards must follow the prompt-card schema headings
- README Quick start relative links must resolve (and #anchors must exist)

Usage:
  python scripts/playbook_lint.py

Exit codes:
  0 OK
  1 Lint errors found
  2 Fatal error (e.g., bad repo layout)
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


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


def _fail(errors: List[str], msg: str) -> None:
    errors.append(msg)


def _load_manifest(path: Path, errors: List[str]) -> Optional[TopicManifest]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        _fail(errors, f"{path}: invalid JSON ({e})")
        return None

    required = [
        "status",
        "canonical_instructions_file",
        "canonical_knowledge_files",
        "router_path",
        "prompt_cards",
    ]
    for k in required:
        if k not in data:
            _fail(errors, f"{path}: missing required key '{k}'")
            return None

    prompt_cards: List[PromptCard] = []
    pcs = data.get("prompt_cards") or []
    if not isinstance(pcs, list):
        _fail(errors, f"{path}: 'prompt_cards' must be a list")
        return None
    for i, pc in enumerate(pcs):
        if not isinstance(pc, dict):
            _fail(errors, f"{path}: prompt_cards[{i}] must be an object")
            return None
        file = (pc.get("file") or "").strip()
        purpose = (pc.get("purpose") or "").strip()
        if not file:
            _fail(errors, f"{path}: prompt_cards[{i}] missing 'file'")
            return None
        prompt_cards.append(PromptCard(file=file, purpose=purpose))

    topic = (data.get("topic") or path.parent.name).strip()
    status = (data.get("status") or "scaffold").strip().lower()
    if status not in {"complete", "scaffold"}:
        _fail(errors, f"{path}: status must be 'complete' or 'scaffold' (got '{status}')")
        return None

    return TopicManifest(
        topic=topic,
        status=status,
        canonical_instructions_file=str(data.get("canonical_instructions_file") or "").strip(),
        canonical_knowledge_files=list(data.get("canonical_knowledge_files") or []),
        router_path=str(data.get("router_path") or "").strip(),
        prompt_cards=prompt_cards,
    )


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _extract_router_allowlist_filenames(router_text: str) -> Set[str]:
    """
    Extract backticked markdown filenames from router text.

    Accepts both:
      - `decision_memo.md`
      - `prompts/decision_memo.md`

    Returns basenames only (e.g. 'decision_memo.md').
    """
    raw = re.findall(r"`([^`]+?\.md)`", router_text)
    return {Path(x).name for x in raw}


def _prompt_schema_ok(prompt_text: str) -> Tuple[bool, List[str]]:
    missing: List[str] = []

    def has_heading_or_label(name: str) -> bool:
        # accepts either "## Best for" or "**Best for:**"
        heading = re.search(rf"^##\s+{re.escape(name)}\s*$", prompt_text, flags=re.M | re.I)
        label = re.search(rf"^\*\*{re.escape(name)}:\*\*\s+.+$", prompt_text, flags=re.M | re.I)
        return bool(heading or label)

    for name in ["Best for", "You provide", "Output"]:
        if not has_heading_or_label(name):
            missing.append(name)

    if not re.search(r"^##\s+Prompt Template\b", prompt_text, flags=re.M | re.I):
        missing.append("Prompt Template")

    # Template subheadings (enforce for consistency)
    required_sub = [
        "### Role",
        "### Task",
        "### Inputs",
        "### Constraints",
        "### Output Format (strict)",
        "### Verification checklist",
    ]
    for sub in required_sub:
        if sub.lower() not in prompt_text.lower():
            missing.append(sub)

    return (len(missing) == 0), missing


def _github_anchor(text: str) -> str:
    # Approximate GitHub heading -> anchor conversion
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s


def _anchors_in_markdown(md_text: str) -> Set[str]:
    anchors: Set[str] = set()
    for line in md_text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not m:
            continue
        heading = m.group(2)
        anchors.add(_github_anchor(heading))
    return anchors


def _lint_quick_start_links(readme_path: Path, errors: List[str]) -> None:
    txt = _read_text(readme_path)
    m = re.search(r"^##\s+Quick start\s*$", txt, flags=re.M | re.I)
    if not m:
        return

    # Section body until next level-2 heading
    section_start = txt.find("\n", m.end())
    if section_start == -1:
        return
    next_h2 = re.search(r"^##\s+", txt[section_start + 1 :], flags=re.M)
    section_end = (section_start + 1 + next_h2.start()) if next_h2 else len(txt)
    body = txt[section_start:section_end]

    # Find markdown links
    for label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", body):
        if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
            continue
        # Ignore purely external anchors (rare)
        if target.startswith("#"):
            anchor = target[1:]
            anchors = _anchors_in_markdown(txt)
            if anchor not in anchors:
                _fail(errors, f"{readme_path}: Quick start link #{anchor} does not match any heading in this README")
            continue

        # Path (+ optional anchor)
        if "#" in target:
            rel_path, anchor = target.split("#", 1)
        else:
            rel_path, anchor = target, ""

        # Resolve relative to the README's directory
        resolved = (readme_path.parent / rel_path).resolve()
        if not resolved.exists():
            _fail(errors, f"{readme_path}: Quick start link target does not exist: {target}")
            continue

        if anchor:
            md = _read_text(resolved)
            anchors = _anchors_in_markdown(md)
            if anchor not in anchors:
                _fail(errors, f"{readme_path}: Quick start link anchor not found: {target}")


def _lint_topic(repo_root: Path, topic_dir: Path, manifest: TopicManifest, errors: List[str]) -> None:
    # Validate referenced files exist
    if not manifest.canonical_instructions_file:
        _fail(errors, f"{topic_dir}: manifest canonical_instructions_file is empty")
    else:
        instr_path = topic_dir / manifest.canonical_instructions_file
        if not instr_path.exists():
            _fail(errors, f"{topic_dir}: canonical_instructions_file not found: {manifest.canonical_instructions_file}")

        # Prevent drift: extra non-DEPRECATED instructions files not referenced
        instr_dir = topic_dir / "gpt-instructions"
        if instr_dir.exists():
            extras = [
                p.name
                for p in instr_dir.glob("*.md")
                if "DEPRECATED" not in p.name.upper() and p.name != Path(manifest.canonical_instructions_file).name
            ]
            if extras:
                _fail(errors, f"{topic_dir}: extra instructions files not in manifest: {extras}")

    if not manifest.router_path:
        _fail(errors, f"{topic_dir}: manifest router_path is empty")
    else:
        router_path = topic_dir / manifest.router_path
        if not router_path.exists():
            _fail(errors, f"{topic_dir}: router_path not found: {manifest.router_path}")

    if not manifest.canonical_knowledge_files:
        _fail(errors, f"{topic_dir}: manifest canonical_knowledge_files is empty")
    else:
        for k in manifest.canonical_knowledge_files:
            kp = topic_dir / k
            if not kp.exists():
                _fail(errors, f"{topic_dir}: canonical_knowledge_file not found: {k}")

        # Prevent drift: extra knowledge files not referenced
        knowledge_dir = topic_dir / "knowledge"
        if knowledge_dir.exists():
            referenced = {Path(k).name for k in manifest.canonical_knowledge_files}
            extras = [p.name for p in knowledge_dir.glob("*.md") if p.name not in referenced]
            if extras:
                _fail(errors, f"{topic_dir}: extra knowledge files not in manifest: {extras}")

    # Prompt cards
    if not manifest.prompt_cards:
        _fail(errors, f"{topic_dir}: manifest prompt_cards is empty")
    else:
        prompts_dir = topic_dir / "prompts"
        referenced_prompt_files = {pc.file for pc in manifest.prompt_cards}
        # Prevent drift: extra prompt files not referenced
        if prompts_dir.exists():
            extras = [p.name for p in prompts_dir.glob("*.md") if p.name not in referenced_prompt_files]
            if extras:
                _fail(errors, f"{topic_dir}: extra prompt card files not in manifest: {extras}")

        for pc in manifest.prompt_cards:
            pp = prompts_dir / pc.file
            if not pp.exists():
                _fail(errors, f"{topic_dir}: prompt card not found: prompts/{pc.file}")
                continue
            ok, missing = _prompt_schema_ok(_read_text(pp))
            if not ok:
                _fail(errors, f"{topic_dir}: prompt card schema fail: prompts/{pc.file} missing {missing}")

    # If complete, enforce >=3 prompt cards and presence of key assets
    if manifest.status == "complete":
        if len(manifest.prompt_cards) < 3:
            _fail(errors, f"{topic_dir}: status=complete requires >=3 prompt cards (found {len(manifest.prompt_cards)})")

        # router + allowlist lint
        router_path = topic_dir / manifest.router_path
        if router_path.exists():
            allowlisted = _extract_router_allowlist_filenames(_read_text(router_path))
            referenced = {pc.file for pc in manifest.prompt_cards}

            for fname in sorted(allowlisted):
                if fname not in referenced:
                    _fail(errors, f"{topic_dir}: router allowlist references prompt not in manifest: {fname}")
                p = topic_dir / "prompts" / fname
                if not p.exists():
                    _fail(errors, f"{topic_dir}: router allowlist references missing prompt file: {fname}")

    # Quick start links in README
    _lint_quick_start_links(topic_dir / "README.md", errors)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    gpts_dir = repo_root / "gpts"
    if not gpts_dir.exists():
        print("Fatal: repo layout missing gpts/ directory")
        return 2

    errors: List[str] = []

    for topic_dir in sorted([p for p in gpts_dir.iterdir() if p.is_dir()]):
        manifest_path = topic_dir / "topic_manifest.json"
        if not manifest_path.exists():
            _fail(errors, f"{topic_dir}: missing topic_manifest.json")
            continue

        manifest = _load_manifest(manifest_path, errors)
        if manifest is None:
            continue

        _lint_topic(repo_root, topic_dir, manifest, errors)

    if errors:
        print("Playbook lint failed:\n")
        for e in errors:
            print(f"- {e}")
        return 1

    print("Playbook lint OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
