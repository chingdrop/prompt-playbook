# Test Plan & Validation — What to Test, How to Prove It Works

**Best for:** creating a verification plan for a change when tests are missing or unclear  
**You provide:** feature/change description, risk areas, environment  
**Output:** prioritized test plan + cases + tooling + acceptance checks  

## Prompt Template (copy/paste)

### Role
You are a test-minded engineer.

### Change summary
[What changed and why.]

### Inputs
- Affected areas/modules:  
- Risk areas (auth, data integrity, performance, migrations):  
- Environment constraints (CI, local only, staging available):  
- Existing tests (if any):  

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
