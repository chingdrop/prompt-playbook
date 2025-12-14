# Pricing Itemization — Clean Materials + Labor Totals

**Best for:** turning a messy list of materials and labor into clean line items  
**You provide:** materials list and labor assumptions  
**Output:** itemized pricing + subtotals + total + notes  

## Prompt Template (copy/paste)

### Role

You are preparing client-ready pricing.

### Task

Turn the provided materials and labor assumptions into clean, client-ready line items with subtotals and a total.

### Inputs

- Materials list (qty, description, unit price; paste raw):
- Labor (hours and rate OR fixed fee):
- Tax/shipping (if any):
- Notes/assumptions:

### Constraints

- Do not invent facts, metrics, dates, pricing, or commitments.
- Ask up to 3 clarifying questions only if required to proceed.
- If assumptions are required, list them (max 5) and proceed.
- If required info is missing, use placeholders like [CLIENT NAME], [DATE], [PRICE], [LOCATION].
- Keep code blocks and quoted text unchanged unless explicitly asked.

### Output Format (strict)

**Materials**

- Item: ... | Quantity: ... | Unit price: ... | Line total: ...
- Subtotal (materials): ...

**Labor**

- ...

**Total**

- ...

**Notes**

- ...

### Verification checklist

- [ ] No invented quantities/prices; placeholders used where needed
- [ ] Subtotals and total reconcile with line items
- [ ] Notes call out assumptions and missing inputs
- [ ] Output matches the required pricing structure
