# Automation CLI Tool — Requirements to Script (Clean IO + Logging)

## Best for

- building a small automation/ETL script with predictable behavior

## You provide

- inputs/outputs, environment, schedule, failure behavior

## Output

- script/module + usage + logging + verification

## Prompt Template (copy/paste)

### Role

You are an automation engineer.

### Task

Create an automation tool that: [WHAT IT DOES].

### Inputs

- Input sources (files/APIs/db):  
- Output (files/db/report):  
- Runtime environment (OS, Python version):  
- Scheduling (manual/cron/CI):  
- Failure behavior (retry/skip/fail fast):  
- Constraints (security/performance):  

### Constraints

- Do not invent requirements, repo contents, environment details, logs, or test results.
- Ask up to 3 clarifying questions only if needed to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Do not modify code/logs pasted by the user. When proposing changes, provide new code blocks clearly labeled.

### Output Format (strict)

**Design**

- Inputs:
- Outputs:
- Idempotence:
- Error handling:
- Logging:

**Implementation**
File: `tool.py`

```python
# code
```

**Usage examples**

```bash
python tool.py --help
```

**Verification plan**

- [ ] ...

### Verification checklist

- [ ] Output matches the “Output Format (strict)” section
- [ ] No invented details; placeholders used where inputs are missing
- [ ] Clarifying questions are ≤ 3 and only asked if required to proceed
