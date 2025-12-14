# Prompt Card Schema (Repository Standard)

This repo enforces **one** prompt card schema for all topics to keep routing, testing, and copy/paste workflows predictable.

Prompt cards live under:

- `gpts/<topic>/prompts/*.md`

If you need to capture “document type”, “audience”, or similar metadata, include it under **Task** and/or **Inputs** (do not introduce alternate section schemas).

## Required sections (in order)

1. Title (H1)
2. `**Best for:**`
3. `**You provide:**`
4. `**Output:**`
5. `## Prompt Template (copy/paste)` containing:
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
- Do not invent facts, metrics, dates, pricing, commitments, logs, or repo contents.
- Ask up to 3 clarifying questions only if needed to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Preserve pasted text/logs/code when quoting; provide changed code in clearly labeled new blocks.

### Output Format (strict)
<Define the exact headings/table/bullets to output.>
<If not needed, state: “Use a clean, skimmable structure with headings.”>

### Verification checklist
- [ ] No invented details; placeholders used for missing inputs
- [ ] Output matches the requested format
- [ ] Next steps / tests included when relevant
- [ ] Internal links are valid and consistent (if applicable)

## Notes (optional)
- <tips, variants, examples>
```

## Link rules for prompt cards

- Real internal refs become links: [`docs/testing_checklist.md`](docs/testing_checklist.md)
- Placeholders stay inline code: `gpts/<topic>/...`
