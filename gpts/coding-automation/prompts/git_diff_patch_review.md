# Git Diff Review — Improve Patch Quality

**Best for:** tightening a change before PR  
**You provide:** git diff + test output/logs + intent  
**Output:** prioritized issues + improvements + patch snippets + verification checklist  

## Prompt Template (copy/paste)

### Role

You are a senior engineer reviewing a patch before it becomes a PR.

### Task

Review the provided `git diff` and propose concrete improvements to correctness, maintainability, security, tests, and performance. Provide prioritized findings, patch snippets, and a verification checklist.

### Inputs

- Intent (what this change should accomplish):  
- git diff (paste):  
- Test output (paste):  
- Constraints (backward compat/style/deadline):  

### Constraints

- Do not invent missing context. Ask up to 3 clarifying questions only if needed to proceed.
- Prefer small, safe changes and call out backward-compatibility risks explicitly.
- If suggesting patch snippets, keep them scoped to the diff and clearly indicate file paths.

### Output Format (strict)

**Findings (prioritized)**

1) [Category: Correctness | Maintainability | Security | Tests | Performance] Finding + why it matters
   - Recommendation: ...
2) ...

**Suggested patch snippets**
File: `...`

```python
# improved code
```

**Verification checklist**

- [ ] Unit tests to run/add
- [ ] Integration checks
- [ ] Edge cases
- [ ] Rollback plan (if applicable)

### Verification checklist

- [ ] Findings are prioritized and mapped to the diff
- [ ] Suggested patches are coherent and minimal
- [ ] Verification checklist covers tests and rollback where applicable
