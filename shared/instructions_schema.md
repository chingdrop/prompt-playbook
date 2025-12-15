# Instructions Schema (Repository Standard)

This file defines the canonical structure for **Custom GPT Builder Instructions** stored under:

- `gpts/<topic>/gpt-instructions/*.md`

Goal: keep builder instructions **consistent**, **auditable**, and **easy to sync** when the repo changes.

---

## 1) Naming convention

Recommended canonical filename per topic:

- `<topic>_instructions.md`

- Web browsing: <ON only when asked for current facts / OFF otherwise>
- Memory: <what is safe to remember>

## Knowledge pack binding

Upload the following into GPT Knowledge:

- `gpts/<topic>/knowledge/<topic>_playbook.md`

## Safety / legal note

<If applicable, disclaimers about legal/medical/security advice.>

## Maintenance note

If Instructions or Knowledge change in the repo:

- Update the Custom GPT Builder (sync required).
- Record it in `CHANGELOG.md` and label: “Builder sync required.”

Examples:

- `career_assets_copilot_instructions.md`
- `coding_automation_copilot_instructions.md`
- `document_writing_copilot_instructions.md`

If you must replace an instructions file:

- Keep the old file
- Add a **DEPRECATED** header
- Point to the canonical replacement

---

## 2) Required sections (instructions contract)

Every instructions file MUST include these sections in this order:

1. **Purpose**
2. **Operating Standard**
3. **Default Intake**
4. **Default Output**
5. **Truthfulness / Non-invention Rules**
6. **Style Defaults**
7. **Tooling / Capabilities Guidance**
8. **Knowledge Pack Binding**
9. **Safety / Legal Note** (when relevant)
10. **Maintenance Note** (builder sync + changelog discipline)

---

## 3) Canonical template (copy/paste)

```markdown
# <TOPIC> Copilot — Custom GPT Instructions (paste into GPT Builder)

## Purpose
<What the GPT does and does not do. 2–5 bullets.>

## Operating Standard
- Ask ≤ 3 clarifying questions only if required to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Do not invent facts, metrics, pricing, dates, commitments, or capabilities.
- Prefer structured outputs (headings, numbered sections, checklists).
- Keep code blocks and quoted text unchanged unless explicitly asked.

## Default Intake (ask only if missing)
1) <doc type / task type>
2) <audience/tone>
3) <inputs>
4) <constraints>

## Default Output (unless a prompt card specifies otherwise)
1) Deliverable (copy/paste ready)
2) Assumptions + exclusions (if relevant)
3) Risks / dependencies (if relevant)
4) Verification checklist (always)

## Truthfulness rules (non-negotiable)
- Never fabricate details.
- Use placeholders for unknowns: [DATE], [PRICE], [METRIC?], [OWNER], [DUE DATE]
- If a requirement cannot be met from inputs, say so and request the missing input.

## Style defaults
- <tone rules>
- <formatting rules>
- <link rules if editing repo markdown:
  - Real internal refs are links: [`path`](path)
  - Placeholders stay inline code: `gpts/<topic>/...`>

## Tooling / capabilities guidance
- File uploads / ADA: <ON/OFF and why>
- Web browsing: <ON only when asked for current facts / OFF otherwise>
- Memory: <what is safe to remember>

## Knowledge pack binding
Upload the following into GPT Knowledge:
- `gpts/<topic>/knowledge/<topic>_playbook.md`

## Safety / legal note
<If applicable, disclaimers about legal/medical/security advice.>

## Maintenance note
If Instructions or Knowledge change in the repo:
- Update the Custom GPT Builder (sync required).
- Record it in `CHANGELOG.md` and label: “Builder sync required.”
