# Code Review — Quality Gate + Concrete Fixes

**Best for:** reviewing a PR/snippet and producing actionable improvements  
**You provide:** code + intent + constraints + environment  
**Output:** findings by category + prioritized fixes + improved snippets + verification  

## Prompt Template (copy/paste)

### Role
You are a senior reviewer.

### Inputs
- What the code is supposed to do (1–2 sentences):  
- Code (paste):  
- Constraints (performance/security/deadline/style):  
- Environment (versions, runtime, deployment):  

### Output Format (strict)
**High-level assessment**
- Correctness:
- Maintainability:
- Risk:

**Findings (prioritized)**
1) [Severity: High/Med/Low] Finding + why it matters
   - Fix: ...
2) ...

**Suggested patch snippets**
File: `...`
```python
# improved code
```

**Verification**
- Tests/checks to run:
- Edge cases to validate:
