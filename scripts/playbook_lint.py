#!/usr/bin/env python3
"""Repo-wide lint for prompt playbook consistency.

Fails if:
- A topic marked **Status:** complete is missing required components.
- Router allowlist references prompt cards that don't exist.
- Prompt cards don't follow the required schema headings.
- README Quick start relative links are broken.

Stdlib-only (for CI portability).
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Set, Tuple


RE_STATUS = re.compile(r"\*\*Status:\*\*\s*(?P<status>\S+)", re.IGNORECASE)
RE_MD_LINK = re.compile(r"\[[^\]]+\]\((?P<target>[^)]+)\)")
RE_HEADING = re.compile(r"^(?P<level>#{1,6})\s+(?P<text>.+?)\s*$")
RE_ROUTER_ALLOW = re.compile(r"→\s*`(?P<card>[^`]+)`")

RE_H2_BEST_FOR = re.compile(r"^##\s+Best\s+for\s*$", re.IGNORECASE)
RE_H2_YOU_PROVIDE = re.compile(r"^##\s+You\s+provide\s*$", re.IGNORECASE)
RE_H2_OUTPUT = re.compile(r"^##\s+Output\s*$", re.IGNORECASE)
RE_H2_PROMPT_TEMPLATE = re.compile(r"^##\s+Prompt\s+Template\b", re.IGNORECASE)

RE_H3_ROLE = re.compile(r"^###\s+Role\s*$", re.IGNORECASE)
RE_H3_TASK = re.compile(r"^###\s+Task\s*$", re.IGNORECASE)
RE_H3_INPUTS = re.compile(r"^###\s+Inputs\s*$", re.IGNORECASE)
RE_H3_CONSTRAINTS = re.compile(r"^###\s+Constraints\s*$", re.IGNORECASE)
RE_H3_OUTPUT_FMT = re.compile(r"^###\s+Output\s+Format\b", re.IGNORECASE)
RE_H3_VERIFY = re.compile(r"^###\s+Verification\s+checklist\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class LintError:
    path: Path
    message: str

    def format(self, root: Path) -> str:
        try:
            rel = self.path.relative_to(root)
        except Exception:
            rel = self.path
        return f"{rel}: {self.message}"


def repo_root(default_from: Optional[Path] = None) -> Path:
    if default_from is None:
        default_from = Path(__file__).resolve()
    # scripts/playbook_lint.py -> repo root
    return default_from.parents[1]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def find_quick_start_section(readme_text: str) -> Optional[str]:
    lines = readme_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s+Quick start\s*$", line, re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if re.match(r"^##\s+", lines[j]):
            end = j
            break
    return "\n".join(lines[start:end]).strip("\n")


def github_slugify(text: str) -> str:
    """Approximate GitHub heading anchor generation.

    Good enough for repo-internal lint (common headings).
    """
    t = text.strip().lower()

    # Drop trailing hashes like "Heading ###"
    t = re.sub(r"\s+#+\s*$", "", t).strip()

    # GitHub strips punctuation; keep alnum, spaces, hyphens.
    t = re.sub(r"[^a-z0-9\s\-]", "", t)
    t = re.sub(r"\s+", "-", t)
    t = re.sub(r"-+", "-", t).strip("-")
    return t


def extract_heading_slugs(md_text: str) -> Set[str]:
    slugs: Set[str] = set()
    counts: dict[str, int] = {}
    for line in md_text.splitlines():
        m = RE_HEADING.match(line)
        if not m:
            continue
        title = m.group("text").strip()
        base = github_slugify(title)
        if not base:
            continue
        n = counts.get(base, 0)
        if n == 0:
            slugs.add(base)
        else:
            slugs.add(f"{base}-{n}")
        counts[base] = n + 1
    return slugs


def is_external_link(target: str) -> bool:
    t = target.strip()
    return bool(re.match(r"^(https?://|mailto:)", t, re.IGNORECASE))


def check_quick_start_links(readme_path: Path, root: Path) -> List[LintError]:
    errors: List[LintError] = []
    txt = read_text(readme_path)
    section = find_quick_start_section(txt)
    if not section:
        return errors

    headings_cache: dict[Path, Set[str]] = {}

    for m in RE_MD_LINK.finditer(section):
        target = m.group("target").strip()
        if not target or is_external_link(target):
            continue

        # Ignore image links/data URIs
        if target.startswith("data:"):
            continue

        file_part, frag = (target.split("#", 1) + [""])[:2]
        frag = frag.strip()

        # same-file anchor
        if file_part.strip() == "":
            file_path = readme_path
        else:
            if file_part.startswith("/"):
                errors.append(LintError(readme_path, f"Quick start link is absolute: ({target})"))
                continue
            file_path = (readme_path.parent / file_part).resolve()

        # Existence check (file or directory)
        if file_part.strip() != "":
            if not file_path.exists():
                errors.append(LintError(readme_path, f"Quick start link target not found: ({target})"))
                continue

        # Anchor check
        if frag:
            anchor = frag.lstrip("#")
            if file_path not in headings_cache:
                try:
                    headings_cache[file_path] = extract_heading_slugs(read_text(file_path))
                except IsADirectoryError:
                    headings_cache[file_path] = set()
            if anchor not in headings_cache[file_path]:
                errors.append(
                    LintError(
                        readme_path,
                        f"Quick start link anchor not found in {file_path.relative_to(root)}: #{anchor}",
                    )
                )

    return errors


def check_topic_complete(topic_dir: Path, root: Path) -> List[LintError]:
    errors: List[LintError] = []

    router = topic_dir / "router" / "00_router.md"
    if not router.exists():
        errors.append(LintError(topic_dir, "Missing router/00_router.md (topic marked complete)"))
    prompts_dir = topic_dir / "prompts"
    if not prompts_dir.exists():
        errors.append(LintError(topic_dir, "Missing prompts/ (topic marked complete)"))

    prompt_cards: List[Path] = []
    if prompts_dir.exists():
        prompt_cards = [
            p for p in sorted(prompts_dir.glob("*.md"))
            if p.is_file() and p.name.lower() != "readme.md"
        ]
        if len(prompt_cards) < 3:
            errors.append(
                LintError(
                    prompts_dir,
                    f"Expected ≥3 prompt cards in prompts/ but found {len(prompt_cards)} (topic marked complete)",
                )
            )

    knowledge_dir = topic_dir / "knowledge"
    if not knowledge_dir.exists():
        errors.append(LintError(topic_dir, "Missing knowledge/ (topic marked complete)"))
    else:
        md = [p for p in knowledge_dir.glob("*.md") if p.is_file()]
        if len(md) < 1:
            errors.append(LintError(knowledge_dir, "Expected at least 1 *.md in knowledge/ (topic marked complete)"))

    instr_dir = topic_dir / "gpt-instructions"
    if not instr_dir.exists():
        errors.append(LintError(topic_dir, "Missing gpt-instructions/ (topic marked complete)"))
    else:
        instr_files = [
            p for p in instr_dir.glob("*.md")
            if p.is_file() and "deprecated" not in p.name.lower()
        ]
        if len(instr_files) != 1:
            errors.append(
                LintError(
                    instr_dir,
                    f"Expected exactly 1 canonical instructions file in gpt-instructions/ (non-DEPRECATED), found {len(instr_files)}",
                )
            )

    return errors


def check_router_allowlist(topic_dir: Path, root: Path) -> List[LintError]:
    errors: List[LintError] = []
    router = topic_dir / "router" / "00_router.md"
    if not router.exists():
        return errors

    router_text = read_text(router)
    prompts_dir = topic_dir / "prompts"

    for m in RE_ROUTER_ALLOW.finditer(router_text):
        raw = m.group("card").strip()
        # Resolve card path:
        if "/" in raw or "\\" in raw:
            # Treat as path relative to router file
            cand = (router.parent / raw).resolve()
        else:
            cand = (prompts_dir / raw).resolve()

        if not cand.exists():
            errors.append(
                LintError(router, f"Router allowlist references missing prompt card: `{raw}`")
            )

    return errors


def find_line_index(lines: List[str], pattern: re.Pattern[str]) -> Optional[int]:
    for i, line in enumerate(lines):
        if pattern.match(line.strip()):
            return i
    return None


def check_prompt_card_schema(card_path: Path) -> List[LintError]:
    errors: List[LintError] = []
    lines = read_text(card_path).splitlines()

    # Must start with an H1 title as first non-empty line.
    first_non_empty = next((l for l in lines if l.strip()), "")
    if not first_non_empty.startswith("# "):
        errors.append(LintError(card_path, "Prompt card must start with an H1 title (# ...)"))

    i_best = find_line_index(lines, RE_H2_BEST_FOR)
    i_you = find_line_index(lines, RE_H2_YOU_PROVIDE)
    i_out = find_line_index(lines, RE_H2_OUTPUT)
    i_tpl = find_line_index(lines, RE_H2_PROMPT_TEMPLATE)

    missing = []
    if i_best is None:
        missing.append("## Best for")
    if i_you is None:
        missing.append("## You provide")
    if i_out is None:
        missing.append("## Output")
    if i_tpl is None:
        missing.append("## Prompt Template")
    if missing:
        errors.append(LintError(card_path, f"Missing required headings: {', '.join(missing)}"))
        return errors

    if not (i_best < i_you < i_out < i_tpl):
        errors.append(
            LintError(
                card_path,
                "Required headings must appear in order: Best for → You provide → Output → Prompt Template",
            )
        )

    # Prompt Template must include required subheadings (H3) within its section.
    # Determine section bounds: from Prompt Template line to next H2 or EOF
    section_lines = lines[i_tpl + 1 :]
    for j, line in enumerate(section_lines):
        if line.strip().startswith("## "):
            section_lines = section_lines[:j]
            break

    required_h3 = [
        (RE_H3_ROLE, "### Role"),
        (RE_H3_TASK, "### Task"),
        (RE_H3_INPUTS, "### Inputs"),
        (RE_H3_CONSTRAINTS, "### Constraints"),
        (RE_H3_OUTPUT_FMT, "### Output Format (strict)"),
        (RE_H3_VERIFY, "### Verification checklist"),
    ]
    for pat, label in required_h3:
        if not any(pat.match(l.strip()) for l in section_lines):
            errors.append(LintError(card_path, f"Prompt Template missing required subheading: {label}"))

    return errors


def lint_repo(root: Path) -> List[LintError]:
    errors: List[LintError] = []
    gpts_dir = root / "gpts"
    if not gpts_dir.exists():
        return [LintError(root, "Missing gpts/ directory")]

    for topic_dir in sorted([p for p in gpts_dir.iterdir() if p.is_dir()]):
        readme = topic_dir / "README.md"
        if not readme.exists():
            errors.append(LintError(topic_dir, "Missing README.md"))
            continue

        txt = read_text(readme)
        m = RE_STATUS.search(txt)
        status = (m.group("status") if m else "").strip().lower()

        # README Quick start link lint (always)
        errors.extend(check_quick_start_links(readme, root))

        # Router allowlist lint (always, if router exists)
        errors.extend(check_router_allowlist(topic_dir, root))

        # Prompt card schema lint (always, if prompts exist)
        prompts_dir = topic_dir / "prompts"
        if prompts_dir.exists():
            for card in sorted([p for p in prompts_dir.glob("*.md") if p.is_file() and p.name.lower() != "readme.md"]):
                errors.extend(check_prompt_card_schema(card))

        # Completeness lint (only for complete topics)
        if status == "complete":
            errors.extend(check_topic_complete(topic_dir, root))

    return errors


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Repo-wide prompt playbook lint.")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repo root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve() if args.root else repo_root()
    errors = lint_repo(root)

    if errors:
        print("Playbook lint failed:\n", file=sys.stderr)
        for e in errors:
            print(f"- {e.format(root)}", file=sys.stderr)
        print(f"\n{len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Playbook lint passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
