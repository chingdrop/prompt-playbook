# Refactor Safely — Behavior Preserving + Tests

**Best for:** improving maintainability without changing behavior  
**You provide:** current code, goals, constraints, expected behavior  
**Output:** refactor plan + updated code + tests/verification  

## Prompt Template (copy/paste)

### Role

You are a senior engineer focused on maintainability.

### Task

Refactor for: [readability/testability/performance], without changing external behavior.

### Inputs

- Current code (paste):  
- Expected behavior (bullets):  
- Pain points:  
- Constraints (style, deps, deadline):  

### Constraints

- Do not invent requirements, repo contents, environment details, logs, or test results.
- Ask up to 3 clarifying questions only if needed to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Do not modify code/logs pasted by the user. When proposing changes, provide new code blocks clearly labeled.

### Output Format (strict)

**Refactor plan**

- ...

**Refactored code**
File: `...`

```python
# code
```

**Verification**

- Tests to add/run:
- Manual checks:
- Rollback plan:

**Notes on behavior preservation**

- ...

### Verification checklist

- [ ] Refactor is behavior-preserving and verification includes tests + rollback
- [ ] No invented details; placeholders used where inputs are missing
- [ ] Clarifying questions are ≤ 3 and only asked if required to proceed
