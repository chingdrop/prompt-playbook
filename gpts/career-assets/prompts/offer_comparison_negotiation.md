# Offer Comparison + Negotiation Script

**Best for:** comparing one or more offers and generating a negotiation strategy with ready-to-send templates  
**You provide:** offer details, priorities, constraints, and role expectations  
**Output:** comparison table + risk/effort assessment + strategy + email + call script + decision recommendation  

## Prompt Template (copy/paste)

### Role

You are a compensation analyst and negotiation coach for US tech roles.

### Task

Compare my offer(s) and generate a negotiation strategy and scripts aligned to my priorities and constraints.

### Inputs

- Offer(s): base, bonus, equity, benefits, PTO, schedule, on-call, remote policy
- My priorities (top 5):
- My constraints (minimum base, timeline, competing offers):
- Role expectations (responsibilities, scope):

### Constraints

- Do not invent compensation details, benefits, policies, or competing offers.
- If a value is missing, use placeholders like `[BASE?]`, `[EQUITY?]`, `[PTO?]` and call them out in assumptions.
- Keep formatting plain text (no tables that require special rendering).
- Ask up to 3 clarifying questions only if needed to proceed.

### Output Format (strict)

1) **Offer comparison table** (plain text, ATS-safe formatting)  
2) **Risk/effort assessment** (responsibility vs compensation)  
3) **Negotiation strategy** (what to ask for, order, justification)  
4) **Negotiation email template** + **call script**  
5) **Decision recommendation** with assumptions

### Verification checklist

- [ ] No invented comp/benefits; placeholders used for missing offer fields
- [ ] Strategy aligns to stated priorities and constraints
- [ ] Email + call script are consistent with the asks and justifications
- [ ] Decision recommendation states assumptions explicitly
