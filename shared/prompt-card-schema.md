# Prompt Card Schema (Repository Standard)

This file defines the **canonical structure** for prompt cards stored under:

- `gpts/<topic>/prompts/*.md`

Prompt cards are designed to be:

- **copy/paste ready**
- **ATS / business-safe** (no invented facts)
- **consistent across topics**
- **easy to route** (router selects a filename; user pastes the card)

---

## 1) File naming

Use one of these patterns (pick one per topic and stay consistent):

### Option A — Ordered (recommended for curated libraries)

- `01_<short_name>.md`
- `02_<short_name>.md`

Example:

- `01_resume_tailor_ats.md`
- `05_outreach_email_hiring_manager.md`

### Option B — Descriptive (recommended for growing libraries)

- `<short_name>.md`

Example:

- `debug_triage_ranked_hypotheses.md`
- `repo_markdown_consistency_pass.md`

Rules:

- Use `snake_case`
- Avoid generic names like `prompt.md`, `template.md`
- Keep under ~40 characters when possible

---

## 2) Required sections (prompt card contract)

Every prompt card MUST include these sections in this order:

1. **Title (H1)**
2. **Best for**
3. **You provide**
4. **Output**
5. **Prompt Template (copy/paste)**
6. **Output Format (strict)** *(required when structure matters)*
7. **Quality gates / verification checklist** *(required)*

---

## 3) Canonical template (copy/paste)

Use this template for every new prompt card:

```markdown
# <TITLE>

**Best for:** <one sentence describing when to use this>
**You provide:** <inputs the user must paste; bullets preferred>
**Output:** <what the model returns; be specific>

## Prompt Template (copy/paste)

### Role
<describe the role and domain context in 1–2 lines>

### Task
<exactly what to do>

### Inputs
- <required input 1>
- <required input 2>
- <optional input 1>

### Constraints
- Do not invent facts, metrics, dates, pricing, or capabilities.
- Ask up to 3 clarifying questions only if required to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Keep code blocks and quoted text unchanged unless explicitly asked.
- Use the repo’s link rules:
  - Real internal refs become links: [`docs/x.md`](docs/x.md)
  - Placeholders stay inline code: `gpts/<topic>/...`

### Output Format (strict)
<Define the exact headings/table/bullets to output.>
<If not needed, state: “Use a clean, skimmable structure with headings.”>

### Verification checklist
- [ ] No invented details; placeholders used for missing inputs
- [ ] Output matches the requested format
- [ ] Internal links are valid and consistent (if applicable)
- [ ] Scope boundaries, assumptions, and exclusions are explicit (if applicable)
- [ ] Next steps / tests included (if applicable)

## Notes (optional)
- <any tips, variants, or examples that help the user>
