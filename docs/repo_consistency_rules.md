# Repo Consistency Rules

This file defines repo-wide conventions to keep all topics consistent, linkable, and maintainable.

---

## 1) Folder contract per topic

Every topic folder must exist under:

- `gpts/<topic>/`

**Topic folder naming**

- Topic folder names should be **kebab-case** (example: `gpts/it-delivery/`).
- Markdown filenames inside a topic should be **snake_case** (example: `router/00_router.md`, `prompts/change_plan_with_rollback.md`).

Each topic must include:

- `README.md`
- `gpt-instructions/` (one or more `.md`)
- `router/00_router.md`
- `prompts/` (may be empty only for scaffolds)
- `knowledge/` (optional but strongly recommended)

---

## 2) Status truth rules

Topic README must declare:

- `**Status:** complete|scaffold`

A topic can be labeled **complete** only if it has:

- At least 1 instructions file
- `router/00_router.md`
- At least 3 prompt cards
- At least 1 knowledge file

A topic is a **scaffold** if it has:

- At least 1 instructions file
- `router/00_router.md`
- Fewer than 3 prompt cards and/or no knowledge pack yet

---

## 3) Router contract

The router must live at:

- `gpts/<topic>/router/00_router.md`

Router must output:

1) the chosen prompt card filename  
2) a filled-in prompt template (placeholders allowed)  
3) up to 3 clarifying questions only if required  

Routers should enumerate an explicit allowlist of prompt filenames to prevent hallucinated filenames.

---

## 4) README standards

### Root README (`README.md`)

Root README should:

- explain the repo purpose
- list topics with status
- include the canonical paths for schemas and key docs
- provide a clear “how to use this repo” onboarding path

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

Every prompt card must follow the canonical schema in:

- `shared/prompt_card_schema.md`

Do not create alternate schemas.

Prompt cards must be copy/paste-ready and include:

- a clear “You provide” section
- a clear “Output” section
- a prompt template with:
  - Role
  - Task
  - Inputs
  - Constraints
  - Output Format (strict)
  - Verification checklist

Use strict output formats when the use case benefits from structure.

---

## 6) Maintenance hygiene rules

### Changelog

Update `CHANGELOG.md` for:

- new topics
- schema changes
- changes that require updating deployed Custom GPTs

If the Builder must be updated, label the entry: **Builder sync required**.

### Deprecation policy

If a non-canonical instructions or knowledge file exists:

- Do **not** delete it.
- Add `# DEPRECATED` at the top.
- Point to the canonical replacement file path.

**Canonical filenames**

- Instructions canonical: `gpts/<topic>/gpt-instructions/<topic>_copilot_instructions.md`
- Knowledge canonical: `gpts/<topic>/knowledge/<topic>_playbook.md`

(If a topic has additional instruction/knowledge files, they must be marked DEPRECATED and point to the canonical file.)

---

## 7) Quality gates before merging

Before merging changes:

- Router selects an existing prompt card (from an explicit allowlist)
- Prompt cards are copy/paste-ready and schema-aligned
- README paths are correct
- Status is accurate per “Status truth rules”
- Testing checklist passes (`docs/testing_checklist.md`)
- Changelog updated (and flags Builder sync when required)
