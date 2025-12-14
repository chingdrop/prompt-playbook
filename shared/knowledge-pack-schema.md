# Knowledge Pack Schema

This file defines the canonical structure for **Knowledge Packs** stored under:

- `gpts/<topic>/knowledge/*.md`

Goal: keep knowledge packs **stable**, **scoped**, and **behavior-shaping** (not a dumping ground).

## Naming convention

**Recommended canonical filename per topic**

- `<topic>_playbook.md`

Examples

- `career_assets_playbook.md`
- `coding_automation_playbook.md`
- `document_writing_playbook.md`

**If multiple files are required**, split by function

- `output_schemas.md`
- `glossary.md`
- `style_guide.md`

## Required sections

Every knowledge pack must include these sections **in this order**:

1. Purpose
2. What this GPT is best at
3. Scope boundaries (what it should not do)
4. Default response contract
5. Truthfulness rules (non-negotiable)
6. House style and formatting rules
7. Core procedures (step-by-step playbooks)
8. Quality checks (verification)
9. Update notes (optional but recommended)

## Canonical template (copy/paste)

```markdown
# <TOPIC> Playbook (Knowledge Pack)

Updated: [YYYY-MM-DD]

## Purpose
<What this knowledge pack is intended to standardize.>

## What this GPT is best at
- ...
- ...

## Scope boundaries
- Do not ...
- Out of scope: ...

## Default response contract
Unless the user requests otherwise:
1) Ask up to 3 clarifying questions only if needed.
2) Deliver the requested output (copy/paste ready).
3) List assumptions and exclusions (as applicable).
4) List risks and dependencies (as applicable).
5) Provide a verification checklist.

## Truthfulness rules (non-negotiable)
- Never invent facts, metrics, pricing, dates, tools, capabilities, or commitments.
- Use placeholders when inputs are missing: [DATE], [PRICE], [METRIC?], [OWNER], [DUE DATE].
- If something cannot be concluded from inputs, explicitly request the missing input.

## House style and formatting rules
- Tone: ...
- Formatting: ...
- Link rules (if repo editing):
  - Real internal refs become links: [`path`](path)
  - Placeholders stay inline code: `gpts/<topic>/...`

## Core procedures
### Procedure 1: <name>
1) ...
2) ...
3) ...

### Procedure 2: <name>
1) ...
2) ...
3) ...

## Quality checks
- [ ] No invented details; placeholders used where needed.
- [ ] Output matches the requested format/schema.
- [ ] Assumptions/exclusions are explicit when scope is involved.
- [ ] Links are consistent and valid (if editing markdown).

## Update notes (optional)
- [YYYY-MM-DD] <change>
