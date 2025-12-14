# Meeting Notes — Decisions + Action Items

**Best for:** converting rough notes into clean minutes with owners and due dates  
**You provide:** raw notes, attendees, date, decisions  
**Output:** structured notes + action item table (Markdown)  

## Prompt Template (copy/paste)

### Role

You are a program manager producing meeting minutes.

### Task

Convert the raw notes into structured meeting minutes with decisions, discussion notes, and an action-items table.

### Inputs

- Meeting title:
- Date/time:
- Attendees:
- Raw notes (paste):
- Decisions (if already known):
- Action items (if already known):

### Constraints

- Do not invent facts, metrics, dates, pricing, or commitments.
- Ask up to 3 clarifying questions only if required to proceed.
- If assumptions are required, list them (max 5) and proceed.
- Keep code blocks and quoted text unchanged unless explicitly asked.
- If owners/dates are missing, use placeholders like [OWNER] and [DUE DATE].

### Output Format (strict)

**Summary**

- ...

**Decisions**

- ...

**Discussion Notes**

- ...

**Action Items**

| Action | Owner | Due Date | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

### Verification checklist

- [ ] Owners and due dates captured; placeholders used if missing
- [ ] Decisions are explicit and unambiguous
- [ ] Action items table is complete and readable
- [ ] Output matches the required headings and table format
