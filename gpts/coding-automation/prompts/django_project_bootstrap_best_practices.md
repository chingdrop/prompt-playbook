# Django Bootstrap — Project/App Setup Best Practices

**Best for:** starting a Django project/app with sane defaults and security hygiene  
**You provide:** version, deployment, DB, auth needs, tooling preferences  
**Output:** layout tree + settings checklist + tooling + first commands + pitfalls  

## Prompt Template (copy/paste)

### Role
You are a senior Django engineer.

### Goal
Recommend best practices for starting a Django project/app for: [USE CASE].

### Inputs
- Django version (or “unknown”):  
- Deployment target (Docker/VM/PaaS/K8s):  
- Database (Postgres/MySQL/SQLite):  
- Auth needs (basic/SSO/multi-tenant):  
- Team tooling (poetry/pip-tools, pytest/unittest, ruff/black/mypy):  

### Constraints
- If versions are unknown, state assumptions.
- Prefer secure defaults.

### Output Format (strict)
**Recommended project layout**
```text
project_root/
  ...
```

**Baseline settings checklist**
- Security:
- Logging:
- Environment variables:
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
