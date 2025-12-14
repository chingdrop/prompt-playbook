# Prompt Card Schema (Repository Standard)

This file defines the **single canonical structure** for prompt cards stored under:

- `gpts/<topic>/prompts/*.md`

If you need to capture “document type”, “audience”, or similar metadata, put it under **Task** and/or **Inputs** (do not introduce alternate section schemas).

## Required sections (prompt card contract)

Every prompt card MUST include these sections in this order:

1. **Title (H1)**
2. **Best for**
3. **You provide**
4. **Output**
5. **Prompt Template (copy/paste)** containing:
   - `### Role`
   - `### Task`
   - `### Inputs`
   - `### Constraints`
   - `### Output Format (strict)`
   - `### Verification checklist`

## Canonical template (copy/paste)

```markdown
# <TITLE>

**Best for:** <one sentence describing when to use this>
**You provide:** <inputs the user must paste; bullets preferred>
**Output:** <what the model returns; be specific>

## Prompt Template (copy/paste)

### Role
<describe the role and domain context in 1–2 lines>

### Task
<exactly what to do; include document type + audience if relevant>

### Inputs
- <required input 1>
- <required input 2>
- <optional input 1>

### Constraints
- Do not invent facts, metrics, dates, pricing, or commitments.
- Ask up to 3 clarifying questions only if required to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Keep code blocks and quoted text unchanged unless explicitly asked.
- Use the repo’s link rules:
  - Real internal refs become links: [`docs/testing_checklist.md`](docs/testing_checklist.md)
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
- <tips, variants, examples>
