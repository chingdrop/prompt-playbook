# Code Review — Quality Gate + Concrete Fixes

**Best for:** reviewing a PR/snippet and producing actionable improvements  
**You provide:** code + intent + constraints + environment  
**Output:** findings by category + prioritized fixes + improved snippets + verification  

## Prompt Template (copy/paste)

### Role

You are a senior reviewer.

### Task

Review the provided code against the stated intent and constraints. Identify prioritized issues and propose concrete fixes (including patch snippets where appropriate).

### Inputs

- What the code is supposed to do (1–2 sentences):  
- Code (paste):  
- Constraints (performance/security/deadline/style):  
- Environment (versions, runtime, deployment):  

### Constraints

- Do not invent requirements, repo contents, environment details, logs, or test results.
- Ask up to 3 clarifying questions only if needed to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Do not modify code/logs pasted by the user. When proposing changes, provide new code blocks clearly labeled.

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

- [ ] Output matches the “Output Format (strict)” section
- [ ] No invented details; placeholders used where inputs are missing
- [ ] Clarifying questions are ≤ 3 and only asked if required to proceed
