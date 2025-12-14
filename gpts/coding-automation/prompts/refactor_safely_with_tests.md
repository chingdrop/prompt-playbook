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
- What it should do (expected behavior):  
- Constraints (performance/security/deadline):  
- Known tests (if any):  

### Constraints

- Do not change external behavior unless explicitly requested; call out any behavior changes.
- Ask up to 3 clarifying questions only if needed to proceed.
- Prefer small, testable refactors with clear rollback.

### Output Format (strict)

**Refactor plan**

- Steps:
- Risks:

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

- [ ] Refactor plan is behavior-preserving
- [ ] Updated code is complete and clearly labeled by file
- [ ] Verification includes tests/commands and rollback plan
