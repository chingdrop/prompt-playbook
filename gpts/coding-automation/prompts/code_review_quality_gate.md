# Code Review — Quality Gate + Concrete Fixes

**Best for:** reviewing a PR/snippet and producing actionable improvements  
**You provide:** code + intent + constraints + environment  
**Output:** findings by category + prioritized fixes + improved snippets + verification  

## Prompt Template (copy/paste)

### Role

You are a senior reviewer.

### Task

Review the provided code against the stated intent and constraints. Identify prioritized issues and propose concrete fixes, including patch snippets where appropriate.

### Inputs

- What the code is supposed to do (1–2 sentences):  
- Code (paste):  
- Constraints (performance/security/deadline/style):  
- Environment (versions, runtime, deployment):  

### Constraints

- Do not invent missing context (requirements, env, data). Ask up to 3 clarifying questions only if needed to proceed.
- When you reference the pasted code, quote it accurately; when proposing changes, provide new code blocks clearly labeled.
- Prefer minimal, safe diffs that improve correctness, security, maintainability, and testability.

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

### Verification checklist

- [ ] Findings are prioritized and actionable
- [ ] Patch snippets map to the stated findings
- [ ] Risks and edge cases are called out
- [ ] Verification section includes concrete tests/checks
