# Repo Consistency Rules

This repo is a **prompt-playbook monorepo** for manual Custom GPT setup. These rules keep the repo predictable so the builder workflow remains low-friction and topics do not drift.

Updated: 2025-12-13

---

## 1) Folder contract (non-negotiable)

Every topic under `gpts/<topic>/` MUST include:

- `README.md`
- `gpt-instructions/` (at least one `.md`)
- `router/00-router.md`
- `prompts/` (may be empty only for scaffolds)
- `knowledge/` (optional; recommended for complete topics)

### Required structure

```text
prompt-playbook/
  README.md
  CHANGELOG.md
  docs/
  shared/
  gpts/
    <topic>/
      README.md
      gpt-instructions/
      router/
        00-router.md
      prompts/
      knowledge/
```

---

## 2) Topic status definitions

Each topic MUST declare status in its `gpts/<topic>/README.md`:

- **complete**: has at least:
  - 1 instruction file under `gpt-instructions/`
  - `router/00-router.md`
  - ≥ 3 prompt cards under `prompts/`
  - ≥ 1 knowledge file under `knowledge/` (strongly recommended; required for “complete” label)

- **scaffold**: has:
  - at least 1 instruction file
  - router exists
  - prompt cards and/or knowledge may be missing

### Status rule
Do not label a topic “complete” unless it meets the criteria above.

---

## 3) Naming conventions

### Topic folders
- Use **kebab-case**: `career-assets`, `coding-automation`, `document-writing`, etc.

### Instruction files
- Prefer **snake_case** and be explicit:
  - Good: `coding_automation_copilot_instructions.md`
  - Avoid: `instructions.md` (too generic), unless there is only one topic in the repo.

### Knowledge packs
- Prefer a single “knowledge pack” file when possible:
  - `knowledge/<topic>_playbook.md`
- If multiple knowledge files are needed, keep them narrowly scoped and name them by function:
  - `knowledge/output_schemas.md`, `knowledge/domain_terms.md`

### Prompt cards
- Use descriptive snake_case or ordered naming, but be consistent within the topic.
  - Ordered (good): `01_resume_tailor_ats.md`
  - Descriptive (good): `debug_triage_ranked_hypotheses.md`
- Each prompt card MUST contain:
  - “Best for”, “You provide”, and a **copy/paste prompt template**
  - A **strict output format** when the use case benefits from structure

### Router
- Router file name is always `router/00-router.md`
- Router MUST output:
  1) chosen prompt card filename
  2) a filled-in prompt template (placeholders for missing inputs)
  3) up to 3 clarifying questions (only if required)

---

## 4) README standards

### Root README (`README.md`)
Must include:
- Purpose and scope (manual setup, no APIs)
- Folder structure overview
- List of topics with **accurate statuses**
- Links to:
  - [docs/custom_gpt_integration_guide.md](custom_gpt_integration_guide.md)
  - [docs/testing_checklist.md](testing_checklist.md)
  - [docs/repo_consistency_rules.md](repo_consistency_rules.md)
  - [docs/ai/](ai/README.md) templates

### Topic README (`gpts/<topic>/README.md`)
Must include:
- Title + 1–2 line description
- `**Status:** complete|scaffold`
- “Quick start” with correct file paths:
  - instructions file path (specific filename)
  - knowledge upload (if present)
  - router path
  - prompt cards path
- “Prompt cards” section:
  - for complete topics: list the top 6–12 prompt cards
  - for scaffolds: list “recommended prompt cards to add next”
- “Output quality rules” section

---

## 5) CHANGELOG rules

The repo root MUST contain `CHANGELOG.md` with:

- An **Unreleased** section containing:
  - `### Additions`
  - `### Changes`
  - `### Fixes`

- Release sections named like:
  - `## v0.1.0`, `## v0.2.0`, etc.

### Builder sync rule
If a change requires updating the Custom GPT Builder (Instructions or Knowledge uploads), the change MUST be called out explicitly in the changelog, e.g.:
- “Builder sync required: update Instructions for Coding & Automation Copilot.”

---

## 6) Deprecation policy

Do not delete old instruction files abruptly. If you must replace an instruction file:

- Keep the old file
- Add a **DEPRECATED** header at the top
- Point to the canonical replacement file

---

## 7) Quality gates before merging changes

Before merging changes to any topic:

- [ ] Router selects an existing prompt card file
- [ ] Prompt cards are copy/paste-ready and have strict output formats where appropriate
- [ ] Topic README paths are correct
- [ ] Topic status is accurate (complete vs scaffold)
- [ ] [docs/testing_checklist.md](testing_checklist.md) passes for that topic
- [ ] CHANGELOG updated (and flags Builder sync if required)

---

## 8) Recommended repo hygiene (optional)

These are optional but strongly recommended:

- Add a `.gitignore` (cross-platform)
- Add [docs/testing_checklist.md](testing_checklist.md) and use it after instruction/knowledge updates
- Tag releases (`v0.1.0`, etc.) when behavior changes materially
