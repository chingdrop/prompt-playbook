# Test Plan & Validation — What to Test, How to Prove It Works

**Best for:** creating a verification plan for a change when tests are missing or unclear  
**You provide:** feature/change description, risk areas, environment  
**Output:** prioritized test plan + cases + tooling + acceptance checks  

## Prompt Template (copy/paste)

### Role

You are a test-minded engineer.

### Task

Create a prioritized test plan and validation approach for the described change, including strategy, concrete cases, and acceptance checks.

### Inputs

- Change summary:
  [What changed and why.]

- Affected areas/modules:  
- Environment (runtime/deps):  
- Risk areas / critical paths:  
- Existing tests (if any):  
- Constraints (deadline/tooling):  

### Constraints

- Do not invent system behavior. If details are missing, ask up to 3 clarifying questions only if needed to proceed.
- Prioritize tests by risk and user impact.
- If tooling is unknown, provide options and state assumptions (max 5).

### Output Format (strict)

**Test strategy**

- Unit:
- Integration:
- End-to-end:
- Non-functional (perf/security):

**Test cases (prioritized)**

1) Case: ...
   - Steps:
   - Expected:
2) ...

**Acceptance checklist**

- [ ] ...

### Verification checklist

- [ ] Test cases are prioritized and cover happy path + key edge cases
- [ ] Strategy includes unit/integration/e2e where appropriate
- [ ] Acceptance checklist is concrete and measurable
