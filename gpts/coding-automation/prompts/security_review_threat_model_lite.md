# Security Review — Lite Threat Model + Remediation

**Best for:** quickly identifying security risks in code touching auth/data/secrets  
**You provide:** code + data sensitivity + deployment context  
**Output:** threats + controls + fixes + logging/monitoring guidance  

## Prompt Template (copy/paste)

### Role
You are a security-minded software engineer.

### Inputs
- What data is handled (PII/PHI/secrets/none):  
- Deployment context (local/serverless/container/VM):  
- Code (paste):  
- Auth model (if any):  
- Known constraints:  

### Output Format (strict)
**Assets to protect**
- ...

**Threats (top 5)**
1) ...
2) ...

**Controls / recommendations**
- Input validation:
- AuthZ boundaries:
- Secret handling:
- Logging/monitoring:

**Concrete fixes**
- Patch snippets / config guidance

**Residual risks + next steps**
- ...
