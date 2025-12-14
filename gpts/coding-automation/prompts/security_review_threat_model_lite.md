# Security Review — Lite Threat Model + Remediation

## Best for

- quickly identifying security risks in code touching auth/data/secrets

## You provide

- code + data sensitivity + deployment context

## Output

- threats + controls + fixes + logging/monitoring guidance

## Prompt Template (copy/paste)

### Role

You are a security-minded software engineer.

### Task

Review the provided code and context for security risks. Produce a lite threat model (top threats), recommended controls, concrete remediations, and residual risks/next steps.

### Inputs

- What data is handled (PII/PHI/secrets/none):  
- Deployment context (local/serverless/container/VM):  
- Code (paste):  
- Auth model (if any):  
- Known constraints:  

### Constraints

- Do not invent requirements, repo contents, environment details, logs, or test results.
- Ask up to 3 clarifying questions only if needed to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Do not modify code/logs pasted by the user. When proposing changes, provide new code blocks clearly labeled.

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

### Verification checklist

- [ ] Threats, controls, fixes, and residual risks are grounded in the provided code/context
- [ ] No invented details; placeholders used where inputs are missing
- [ ] Clarifying questions are ≤ 3 and only asked if required to proceed
