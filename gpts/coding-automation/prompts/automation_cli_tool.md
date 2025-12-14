# Automation CLI Tool — Requirements to Script (Clean IO + Logging)

**Best for:** building a small automation/ETL script with predictable behavior  
**You provide:** inputs/outputs, environment, schedule, failure behavior  
**Output:** script/module + usage + logging + verification  

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

- Do not invent APIs, file formats, paths, credentials, or schedules. If missing, ask or use explicit placeholders.
- Ask up to 3 clarifying questions only if needed to proceed.
- Prefer safe defaults: explicit exit codes, clear error messages, and structured logging.
- If you make assumptions, list them (max 5) and proceed.

### Output Format (strict)

**Design**

- Inputs:
- Outputs:
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

- [ ] Inputs/outputs and failure behavior are explicit (no invented details)
- [ ] Usage examples are runnable and match the proposed CLI
- [ ] Logging and error handling are included and consistent
- [ ] Test strategy and acceptance checklist are complete
