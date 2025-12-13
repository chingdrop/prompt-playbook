# Debug Triage — Ranked Hypotheses + Fix Plan

**Best for:** diagnosing errors and unexpected behavior quickly and safely  
**You provide:** stack trace/logs, repro steps, environment, what you tried  
**Output:** ranked causes + diagnostics + fix plan + rollback + verification  

## Prompt Template (copy/paste)

### Role
You are a senior Python/Django engineer.

### Problem
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

### Output Format (strict)
**Symptoms**
- ...

**Top 3 hypotheses (ranked)**
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
