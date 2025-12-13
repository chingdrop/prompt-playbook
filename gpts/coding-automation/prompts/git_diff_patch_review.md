# Git Diff Review — Improve Patch Quality

**Best for:** tightening a change before PR  
**You provide:** git diff + test output/logs + intent  
**Output:** prioritized issues + improvements + patch snippets + verification checklist  

## Prompt Template (copy/paste)

Review this patch and propose concrete improvements.

### Inputs
- Intent (what this change should accomplish):  
- git diff (paste):  
- Test output (paste):  
- Constraints (backward compat/style/deadline):  

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
