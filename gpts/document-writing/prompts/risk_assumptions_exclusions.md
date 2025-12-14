# Assumptions, Exclusions, Risks — Scope Control Package

## Best for

- strengthening proposals/quotes against scope creep

## You provide

- scope and constraints

## Output

- a crisp set of assumptions, exclusions, and risks

## Prompt Template (copy/paste)

### Role

You are a consultant protecting scope while staying reasonable.

### Task

Generate a scope-control package: assumptions, exclusions, and risks/dependencies based on the provided scope and constraints.

### Inputs

- Scope of work (bullets):
- Known constraints (client access, vendor dependencies, hours windows):
- Optional: known risks already identified:

### Constraints

- Do not invent facts, metrics, dates, pricing, or commitments.
- Ask up to 3 clarifying questions only if required to proceed.
- If assumptions are required, list them (max 5) and proceed.
- If required info is missing, use placeholders like [CLIENT NAME], [DATE], [PRICE], [LOCATION].
- Keep code blocks and quoted text unchanged unless explicitly asked.
- Be specific and business-friendly.
- Avoid adversarial tone.

### Output Format (strict)

**Assumptions**

- ...

**Exclusions**

- ...

**Risks / Dependencies**

- ...

### Verification checklist

- [ ] Assumptions/exclusions/risks are specific and non-overlapping
- [ ] No invented details; placeholders used where needed
- [ ] Tone is business-friendly (not adversarial)
- [ ] Output matches the required headings
