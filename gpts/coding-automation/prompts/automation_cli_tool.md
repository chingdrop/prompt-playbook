# Automation CLI Tool — Requirements to Script (Clean IO + Logging)

**Best for:** building a small automation/ETL script with predictable behavior  
**You provide:** inputs/outputs, environment, schedule, failure behavior  
**Output:** script/module + usage + logging + verification  

## Prompt Template (copy/paste)

### Role
You are an automation engineer.

### Goal
Create an automation tool that: [WHAT IT DOES].

### Inputs
- Input sources (files/APIs/db):  
- Output (files/db/report):  
- Runtime environment (OS, Python version):  
- Scheduling (manual/cron/CI):  
- Failure behavior (retry/skip/fail fast):  
- Constraints (security/performance):  

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
