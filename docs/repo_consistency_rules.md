# Repo Consistency Rules

This file defines repo-wide conventions so all GPT topics remain consistent, linkable in Obsidian, and maintainable over time.

Updated: [YYYY-MM-DD]

---

## 1) Folder contract per topic (non-negotiable)

Each topic lives under:

- `gpts/<topic>/`

**Topic folder naming**

- Topic folder names: **kebab-case** (example: `gpts/it-delivery/`)
- Markdown filenames inside a topic: **snake_case** (example: `prompts/change_plan_with_rollback.md`)

Each topic MUST include:

- `README.md`
- `gpt-instructions/` (at least one `.md`)
- `router/00_router.md`
- `prompts/` (may be empty only for scaffolds)
- `knowledge/` (optional but strongly recommended; required for “complete” status)

---

## 2) Status truth rules

Topic README must declare:

- `**Status:** complete|scaffold`

A topic can be labeled **complete** only if it has:

- ≥ 1 instructions file under `gpt-instructions/`
- `router/00_router.md`
- ≥ 3 prompt cards under `prompts/`
- ≥ 1 knowledge file under `knowledge/`

A topic is a **scaffold** if it has:

- ≥ 1 instructions file
- `router/00_router.md`
- fewer than 3 prompt cards and/or no knowledge pack yet

---

## 3) Router contract

The router must live at:

- `gpts/<topic>/router/00_router.md`

Router must:

1) choose exactly one prompt card from an explicit allowlist  
2) ask up to 3 clarifying questions only if required  
3) output:
   - the chosen prompt filename
   - a filled-in prompt template (placeholders allowed)
   - up to 3 clarifying questions (only if required)

Routers should enumerate an explicit allowlist of prompt filenames to prevent hallucinated filenames.

---

## 4) README alignment

### Topic README (`gpts/<topic>/README.md`)

Topic README must:

- declare `**Status:** complete|scaffold`
- include a **Quick start** that references:
  - the canonical instructions file in `gpt-instructions/`
  - the canonical knowledge pack file in `knowledge/`
  - `router/00_router.md`
  - a list of prompt cards (links to `prompts/*.md`)

---

## 5) Prompt card schema contract

All prompt cards must follow:

- `shared/prompt-card-schema.md`

Prompt cards must be copy/paste-ready and include:

- Best for
- You provide
- Output
- Prompt Template (copy/paste), including:
  - Role
  - Task
  - Inputs
  - Constraints
  - Output Format (strict)
  - Verification checklist

---

## 6) Canonical filenames

### Instructions (canonical)

- `gpts/<topic>/gpt-instructions/<topic>_instructions.md`

### Knowledge pack (canonical)

- `gpts/<topic>/knowledge/<topic>_playbook.md`

Notes:

- `<topic>` in filenames should be snake_case (example: `it_delivery_instructions.md`) even when the folder is kebab-case (example: `it-delivery/`).

---

## 7) Deprecation policy

If non-canonical instruction or knowledge files exist:

- Do **not** delete them.
- Add `# DEPRECATED` at the top.
- Point to the canonical replacement file path.

---

## 8) Maintenance hygiene rules

### Changelog discipline

Update `CHANGELOG.md` for:

- new topics
- schema changes
- canonical instructions/knowledge changes
- changes that require updating deployed Custom GPTs

If the Builder must be updated, label the entry: **Builder sync required**.

### Builder sync registry

Maintain a registry of deployed GPTs here:

- `docs/builder_sync.md`

---

## 9) Quality gates before merging

Before merging changes:

- Router selects an existing prompt card (from an explicit allowlist)
- Prompt cards are schema-aligned and copy/paste-ready
- README links resolve (Obsidian + GitHub preview)
- Status is accurate per “Status truth rules”
- Testing checklist passes (`docs/testing_checklist.md`)
- Changelog updated (and flags Builder sync when required)
