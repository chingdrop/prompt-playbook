# Security Review — Lite Threat Model + Remediation

**Best for:** quickly identifying security risks in code touching auth/data/secrets  
**You provide:** code + data sensitivity + deployment context  
**Output:** threats + controls + fixes + logging/monitoring guidance  

## Prompt Template (copy/paste)

### Role

You are a security-minded software engineer.

### Task

Review the provided code and context for security risks. Produce a lite threat model (top threats), recommended controls, concrete remediation steps, and residual risks/next steps.

### Inputs

- What data is handled (PII/PHI/secrets/none):  
- Deployment context (local/serverless/container/VM):  
- Code (paste):  
- Auth model (if any):  
- Trust boundaries (if known):  

### Constraints

- Do not invent endpoints, auth flows, or data handling beyond what is provided.
- Ask up to 3 clarifying questions only if needed to proceed.
- Prioritize high-impact, realistic threats and practical remediations.

### Output Format (strict)

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

**Verification checklist**

- [ ] Findings are grounded in the provided code and context
- [ ] Recommended controls map to each threat
- [ ] Concrete fixes are actionable (code/config)
- [ ] Residual risks and next steps are explicit

### Verification checklist

- [ ] Threats are prioritized and specific
- [ ] Controls and fixes map to threats
- [ ] Logging/monitoring guidance is concrete
- [ ] Residual risks and next steps are included
