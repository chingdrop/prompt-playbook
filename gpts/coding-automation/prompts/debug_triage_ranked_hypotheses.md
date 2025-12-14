# Debug Triage — Ranked Hypotheses + Fix Plan

**Best for:** diagnosing errors and unexpected behavior quickly and safely  
**You provide:** stack trace/logs, repro steps, environment, what you tried  
**Output:** ranked causes + diagnostics + fix plan + rollback + verification  

## Prompt Template (copy/paste)

### Role

You are a senior Python/Django engineer.

### Task

Diagnose the issue using the exact error/trace/logs and provided context. Produce ranked hypotheses, fast diagnostics, a fix plan with rollback, and a verification checklist.

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

- [ ] Hypotheses are ranked with rationale
- [ ] Diagnostics are reversible and ordered by speed/value
- [ ] Fix plan includes rollback
- [ ] Verification checklist is concrete (tests/commands/observable outcomes)
