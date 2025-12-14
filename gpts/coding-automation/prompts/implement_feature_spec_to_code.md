# Implement Feature — Spec to Code (with Tests)

**Best for:** implementing a feature with clear acceptance criteria  
**You provide:** requirements, constraints, interfaces/models, examples  
**Output:** plan + code changes + tests + edge cases + deployment notes  

## Prompt Template (copy/paste)

### Role

You are a pragmatic software engineer.

### Task

Implement the feature described below so it meets the acceptance criteria. Provide a plan, concrete code changes, tests, edge cases/risks, and deployment/config notes.

### Inputs

- Feature goal:
  [One sentence goal.]

- Acceptance criteria:
- [ ] ...
- [ ] ...

- Context:
- Repo/project context (1–3 sentences):  
- Relevant code (paste):  
- Data shapes (examples):  
- Constraints (security/performance/deadline):  

### Constraints

- Do not invent requirements, interfaces, or environment details. Ask up to 3 clarifying questions only if needed to proceed.
- If you must assume, list assumptions (max 5) and proceed.
- Prefer incremental, testable changes. If code cannot be fully implemented here, provide a patch plan and runnable test plan.

### Output Format (strict)

**Plan**

- ...

**Proposed code changes**
File: `path/to/file.py`

```python
# code
```

**Tests**

- Unit tests:
- Integration tests (if applicable):
- If tests cannot be written here, provide a runnable test plan.

**Edge cases + risks**

- ...

**Deployment/config notes**

- ...

### Verification checklist

- [ ] Plan maps directly to acceptance criteria
- [ ] Code changes are clearly scoped to file paths
- [ ] Tests (or runnable test plan) cover key paths and edge cases
- [ ] Risks and deployment/config impacts are called out
