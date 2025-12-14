# Repo Consistency Rules

This file defines repo-wide conventions to keep all topics consistent and maintainable.

---

## 1) Folder contract per topic

Every topic folder must exist under:

- `gpts/<topic>/`

Each topic must include:

- `README.md`
- `gpt-instructions/` (one or more `.md`)
- `router/00-router.md`
- `prompts/` (may be empty only for scaffolds)
- `knowledge/` (optional but strongly recommended)

---

## 2) Status truth rules

Topic README must declare:

- `**Status:** complete|scaffold`

A topic can be labeled **complete** only if it has:

- At least 1 instructions file
- `router/00-router.md`
- At least 3 prompt cards
- At least 1 knowledge file

A topic is a **scaffold** if it has:

- At least 1 instructions file
- `router/00-router.md`

---

## 3) Router contract

The router must live at:

- `gpts/<topic>/router/00-router.md`

Router must output:

1) the chosen prompt card filename  
2) a filled-in prompt template (placeholders allowed)  
3) up to 3 clarifying questions only if required  

---

## 4) README standards

### Root README (`README.md`)

Must include:

- Purpose and scope (manual setup, no APIs)
- Folder structure overview
- List of topics with **accurate statuses**
- Links to:
  - [`docs/custom_gpt_integration_guide.md`](custom_gpt_integration_guide.md)
  - [`docs/testing_checklist.md`](testing_checklist.md)
  - [`docs/repo_consistency_rules.md`](repo_consistency_rules.md)
  - [`docs/ai/README.md`](ai/README.md) templates

Copy/paste targets for the root `README.md` (note the `docs/` prefix):

- `docs/custom_gpt_integration_guide.md`
- `docs/testing_checklist.md`
- `docs/repo_consistency_rules.md`
- `docs/ai/README.md`

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
  - for complete topics: list at least 3 cards
  - for scaffold topics: list “TBD” or a placeholder

---

## 5) Prompt card schema contract

Every prompt card must follow the canonical schema in:

- [`shared/prompt-card-schema.md`](../shared/prompt-card-schema.md)

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

Repo must include `CHANGELOG.md` with:

- `## Unreleased`
- `### Additions`
- `### Changes`
- `### Fixes`
- versioned releases (e.g., `## v0.1.0`)

If Builder needs updating, changelog must explicitly include:

- “Builder sync required: …”

### Deprecation policy

Do not delete replaced instruction files.

If a file is replaced:

- Add `# DEPRECATED` at the top
- Point to the canonical replacement file path

---

## 7) Quality gates before merging

Before merging changes:

- Router selects an existing prompt card
- Prompt cards are copy/paste-ready
- README paths are correct
- Status is accurate
- Testing checklist passes
- Changelog updated (and flags Builder sync when required)
