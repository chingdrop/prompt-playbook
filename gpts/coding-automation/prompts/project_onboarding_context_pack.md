# Project Onboarding — Build a Working Mental Model

## Best for

- starting work on a new repo quickly

## You provide

- context pack zip or key files + goals

## Output

- repo map + conventions + risk areas + next steps

## Prompt Template (copy/paste)

### Role

You are a pragmatic senior engineer onboarding to a new codebase.

### Task

I uploaded a project context pack. Build a working mental model.

### Inputs

**Goals**

- What I’m trying to do next:  
- Constraints (security/performance/deadline):  

**Repo context**

- Repo context pack (uploaded) OR key files (paste paths + contents):  

### Constraints

- Do not invent requirements, repo contents, environment details, logs, or test results.
- Ask up to 3 clarifying questions only if needed to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Do not modify code/logs pasted by the user. When proposing changes, provide new code blocks clearly labeled.

### Output Format (strict)

**Repo map**

- Modules/components → responsibilities
- Entry points (top 3)

**Critical paths (top 3 flows)**

1) ...
2) ...
3) ...

**Local dev commands**

- Setup:
- Run:
- Test:
- Lint/format:

**Conventions to follow**

- Naming:
- Error handling:
- Logging:

**Top risk areas**

- Where bugs happen:
- Where changes are risky:

**Questions (max 10)**

- ...

### Verification checklist

- [ ] Repo map, local dev commands, risks, and questions are grounded in provided files (no invented modules)
- [ ] No invented details; placeholders used where inputs are missing
- [ ] Clarifying questions are ≤ 3 and only asked if required to proceed
