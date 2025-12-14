# Test Plan & Validation — What to Test, How to Prove It Works

## Best for

- creating a verification plan for a change when tests are missing or unclear

## You provide

- feature/change description, risk areas, environment

## Output

- prioritized test plan + cases + tooling + acceptance checks

## Prompt Template (copy/paste)

### Role

You are a test-minded engineer.

### Task

Create a prioritized test plan and validation approach for the described change, including strategy, concrete cases, and acceptance checks.

### Inputs

- Change summary:
  [What changed and why.]
- Affected areas/modules:  
- Risk areas (auth, data integrity, performance, migrations):  
- Environment constraints (CI, local only, staging available):  
- Existing tests (if any):  

### Constraints

- Do not invent requirements, repo contents, environment details, logs, or test results.
- Ask up to 3 clarifying questions only if needed to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Do not modify code/logs pasted by the user. When proposing changes, provide new code blocks clearly labeled.

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

- [ ] Test plan is prioritized by risk and acceptance checks are concrete
- [ ] No invented details; placeholders used where inputs are missing
- [ ] Clarifying questions are ≤ 3 and only asked if required to proceed
