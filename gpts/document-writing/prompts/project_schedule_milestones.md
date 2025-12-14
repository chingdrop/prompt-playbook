# Project Schedule — Milestones + Dependencies

**Best for:** turning a scope into a simple schedule clients can approve  
**You provide:** phases, constraints, lead times, required access  
**Output:** milestone plan + dependency list + acceptance checkpoints  

## Prompt Template (copy/paste)

### Role

You are producing a schedule section for a proposal/SOW.

### Task

Turn the provided scope/phases into a simple milestone schedule with dependencies and acceptance checkpoints.

### Inputs

- Project scope/phases (bullets):
- Target start date (if known):
- Constraints (access windows, site hours, blackout dates):
- Lead times / vendor dependencies (if any):
- Approval gates (if any):

### Constraints

- Do not invent facts, metrics, dates, pricing, or commitments.
- Ask up to 3 clarifying questions only if required to proceed.
- If assumptions are required, list them (max 5) and proceed.
- If required info is missing, use placeholders like [CLIENT NAME], [DATE], [PRICE], [LOCATION].
- Keep code blocks and quoted text unchanged unless explicitly asked.

### Output Format (strict)

**Milestones**

1) ...
2) ...

**Dependencies**

- ...

**Acceptance checkpoints**

- ...

### Verification checklist

- [ ] Milestones are ordered and include dependencies
- [ ] No invented dates; placeholders used where needed
- [ ] Acceptance checkpoints are explicit
- [ ] Output matches the required headings
