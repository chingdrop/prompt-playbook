# Django Bootstrap — Project/App Setup Best Practices

**Best for:** starting a Django project/app with sane defaults and security hygiene  
**You provide:** version, deployment, DB, auth needs, tooling preferences  
**Output:** layout tree + settings checklist + tooling + first commands + pitfalls  

## Prompt Template (copy/paste)

### Role

You are a senior Django engineer.

### Task

Recommend best practices for starting a Django project/app for: [USE CASE]. Include secure defaults, a sensible layout, and a clear first-run checklist.

### Inputs

- Django version (or “unknown”):  
- Deployment target (Docker/VM/PaaS/K8s):  
- Database (Postgres/MySQL/SQLite):  
- Auth needs (basic/SSO/multi-tenant):  
- Team tooling (poetry/pip-tools, pytest/unittest, ruff/black/mypy):  

### Constraints

- If versions are unknown, state assumptions.
- Prefer secure defaults.
- Ask up to 3 clarifying questions only if needed to proceed.
- If versions are unknown, list assumptions (max 5) and proceed.

### Output Format (strict)

**Recommended project layout**

```text
project_root/
  ...
```

**Settings checklist**

- Secrets/env:
- Security headers:
- Auth/session:
- Static/media:
- Database:

**Tooling defaults**

- Formatting/linting:
- Type checking:
- Testing:
- Pre-commit (optional):

**First 10 commands**

1) ...
2) ...

**Common pitfalls**

- ...

**Verification checklist**

- [ ] Assumptions called out when versions are unknown
- [ ] Secure defaults included (settings, secrets, authZ boundaries)
- [ ] First commands are runnable for the chosen tooling
- [ ] Pitfalls and mitigations are explicit

### Verification checklist

- [ ] Output includes layout, settings, tooling, first commands, and pitfalls
- [ ] Security hygiene is covered (secrets, settings, auth/session concerns)
- [ ] Guidance matches the stated deployment target and database
