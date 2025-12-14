# Debug Triage — Ranked Hypotheses + Fix Plan

**Best for:** diagnosing errors and unexpected behavior quickly and safely  
**You provide:** stack trace/logs, repro steps, environment, what you tried  
**Output:** ranked causes + diagnostics + fix plan + rollback + verification  

## Prompt Template (copy/paste)

### Role

You are a senior Python/Django engineer.

### Task

Describe the issue and paste the **exact** error/trace/logs (no screenshots).

### Inputs

- Error/trace/logs (paste):  
- Steps to reproduce:  
- Expected vs actual behavior:  
- Environment (OS, Python, Django, key deps):  
- Recent changes (if any):  
- What I tried:  

### Constraints

- Do not invent missing information.
- Prefer reversible diagnostics and fixes first.
- Ask up to 3 clarifying questions only if needed to proceed.
- If you must assume, list assumptions (max 5).

### Output Format (strict)

**Top hypotheses (ranked)**

1) ... (rationale)
2) ...
3) ...

**Diagnostics (fastest first)**

- Step: ...
  - Expected outcome: ...
  - What it means: ...

**Fix plan + rollback**

- Fix steps: ...
- Rollback: ...

**Verification checklist**

- [ ] ...

### Verification checklist

- [ ] Output includes ranked hypotheses, diagnostics, fix plan + rollback, and a concrete verification checklist
- [ ] No invented details; placeholders used where inputs are missing
- [ ] Clarifying questions are ≤ 3 and only asked if required to proceed
