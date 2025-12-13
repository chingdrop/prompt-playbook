# Refactor Safely — Behavior Preserving + Tests

**Best for:** improving maintainability without changing behavior  
**You provide:** current code, goals, constraints, expected behavior  
**Output:** refactor plan + updated code + tests/verification  

## Prompt Template (copy/paste)

### Role
You are a senior engineer focused on maintainability.

### Goal
Refactor for: [readability/testability/performance], without changing external behavior.

### Inputs
- Current code (paste):  
- Expected behavior (bullets):  
- Pain points:  
- Constraints (style, deps, deadline):  

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
