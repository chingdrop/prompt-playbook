# Project Onboarding — Build a Working Mental Model

**Best for:** starting work on a new repo quickly  
**You provide:** context pack zip or key files + goals  
**Output:** repo map + conventions + risk areas + next steps  

## Prompt Template (copy/paste)

### Role

You are a pragmatic senior engineer onboarding to a new codebase.

### Task

Build a working mental model from the provided context pack or pasted files. Summarize repo structure, key flows, conventions, risks, next steps, and ask up to 10 high-value questions.

### Inputs

- Goals:
- What I’m trying to do next:  
- Constraints (security/performance/deadline):  

- Repo context pack (uploaded) OR key files (paste paths + contents):  

### Constraints

- Do not invent repo contents. If key files are missing, ask for them (up to 3 questions if needed to proceed).
- If commands or tooling are unknown, mark them explicitly as unknown rather than guessing.
- Keep questions to a maximum of 10 and prioritize by impact on next work.

### Output Format (strict)

**Repo map**

- Key modules:
- Data flow:
- Entry points:

**How to run locally**

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

**Verification checklist**

- [ ] Repo map includes key modules and data flow
- [ ] Run/test/lint commands are explicit (or marked as unknown)
- [ ] Top risk areas and next steps are actionable
- [ ] Questions are ≤ 10 and prioritized

### Verification checklist

- [ ] Repo map and conventions are grounded in provided files (no invented modules)
- [ ] Risks and next steps are specific and actionable
- [ ] Questions are ≤ 10 and clearly unblock progress
