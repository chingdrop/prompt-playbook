# Career Assets Copilot

Resumes, LinkedIn, outreach, project case studies, interview prep, and offer negotiation.
**Status:** complete

## Quick start

1. Paste builder instructions from [`gpt-instructions/career_assets_instructions.md`](gpt-instructions/career_assets_instructions.md) into the Custom GPT Builder.
2. Upload [`knowledge/career_assets_playbook.md`](knowledge/career_assets_playbook.md) into GPT Knowledge.
3. Use [`router/00_router.md`](router/00_router.md) to select the right prompt card.
4. Copy a prompt card from [`prompts/`](prompts/), fill placeholders, and run.

## Prompt cards

<!-- BEGIN:prompt-cards (auto-generated) -->
- [`cover_letter.md`](prompts/cover_letter.md) — writing a tailored cover letter that maps to a JD without repeating the resume
- [`interview_prep.md`](prompts/interview_prep.md) — preparing for an upcoming interview with a pitch, likely questions, STAR outlines, and a one-page cheat sheet
- [`linkedin_about.md`](prompts/linkedin_about.md) — generating a keyword-rich LinkedIn headline and an About section aligned to a target role
- [`offer_comparison_negotiation.md`](prompts/offer_comparison_negotiation.md) — comparing one or more offers and generating a negotiation strategy with ready-to-send templates
- [`outreach_email_hiring_manager.md`](prompts/outreach_email_hiring_manager.md) — writing a concise hiring-manager outreach email that is personalized and respectful
- [`recruiter_agency_pitch.md`](prompts/recruiter_agency_pitch.md) — introducing yourself to a recruiting firm with a direct, high-signal email and a short connection note
- [`resume_rewrite_baseline.md`](prompts/resume_rewrite_baseline.md) — producing a strong general-purpose resume for a target role family before tailoring to specific job descriptions
- [`resume_tailor_ats.md`](prompts/resume_tailor_ats.md) — tailoring an existing resume to a specific job description (JD) while staying fully truthful and ATS-friendly
<!-- END:prompt-cards -->

## Output quality rules

- Ask ≤ 3 clarifying questions only when required to proceed.
- If uncertain, list assumptions (max 5).
- Do not invent facts, logs, or metrics. Request inputs.
- Always include a verification plan (tests, checklist, or acceptance criteria).
