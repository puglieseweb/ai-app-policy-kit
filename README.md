# AI App Policy Kit

Fifteen policy templates for small businesses that build or use AI applications. Written in plain English, for UK businesses, free to use and adapt.

Each document is short, has the rules on one page and ends with a register or checklist to fill in. Replace everything in [square brackets] with your own details.

**Download the Word and PDF versions:** https://www.puglieseweb.com/ai-policy-kit

## The documents

| | Document | What it settles |
|---|---|---|
| 01 | [AI acceptable use policy](policies/01-ai-acceptable-use-policy.md) | Which AI tools staff may use, and what may go into them |
| 02 | [Data protection for AI apps](policies/02-data-protection-for-ai-apps.md) | What personal data you hold, why, where, and what reaches an AI supplier |
| 03 | [Access control policy](policies/03-access-control-policy.md) | Who can get in, with their own login and two-step sign-in |
| 04 | [Secrets and API keys policy](policies/04-secrets-and-api-keys-policy.md) | Keys out of the code, narrow, capped and rotated |
| 05 | [AI-written code review standard](policies/05-ai-written-code-review-standard.md) | What a person checks before AI-written code goes live |
| 06 | [Incident response and breach reporting plan](policies/06-incident-response-and-breach-reporting.md) | Who does what when something goes wrong, and the ICO's 72 hours |
| 07 | [Backup and recovery policy](policies/07-backup-and-recovery-policy.md) | Backups that have been restored at least once |
| 08 | [Supplier and AI vendor checklist](policies/08-supplier-and-ai-vendor-checklist.md) | The questions to ask before your data goes to a supplier |
| 09 | [AI risk assessment template](policies/09-ai-risk-assessment-template.md) | What could go wrong with an AI feature, written down before launch |
| 10 | [Data retention and erasure policy](policies/10-data-retention-and-erasure-policy.md) | How long data is kept, and deleting a person's data everywhere |
| 11 | [Logging and monitoring standard](policies/11-logging-and-monitoring-standard.md) | Knowing when someone got in, and what they did |
| 12 | [Change and release policy](policies/12-change-and-release-policy.md) | The steps between "it works on my screen" and customers using it |
| 13 | [Human oversight of AI decisions](policies/13-human-oversight-of-ai-decisions.md) | Where a person must check, approve or be reachable |
| 14 | [Model and prompt security standard](policies/14-model-and-prompt-security-standard.md) | Prompt injection, and limiting what a model can reach and do |
| 15 | [Staff training and awareness record](policies/15-staff-training-record.md) | Evidence that people were told |

## Where to start

You do not need all fifteen on day one.

1. **This week:** 01 (acceptable use), 03 (access) and 04 (secrets). They stop the most common losses and need no technical work beyond switching things on.
2. **This month:** 02 (data protection), 06 (incidents) and 07 (backups). Fill in the data map and the contacts table, and restore one backup.
3. **Before you launch or grow an AI feature:** 08, 09, 13 and 14.
4. **As you settle in:** 05, 10, 11, 12 and 15.

## How to use a template

1. Replace the text in [square brackets]. Delete rules that do not apply to you, and say so rather than leaving a rule you will not follow.
2. Name one owner for each document.
3. Have the person who runs the business approve it, and date it.
4. Fill in the register or checklist at the end. That is the part an insurer, a customer or a regulator will ask to see.
5. Review every 12 months, and after any incident.

## What this is not

These templates are a starting point, not legal advice. They reflect UK law and guidance as we understood it in November 2026, including UK GDPR, the Data Protection Act 2018 and guidance from the ICO and the NCSC. Regulated sectors such as health, finance and work with children have further rules. If in doubt, ask a solicitor or the ICO's small business helpline.

## Contributing

Corrections and improvements are welcome: open an issue or a pull request. Keep the words plain and the documents short.

## Licence

© 2026 PuglieseWeb LTD. Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You may copy, change and share these documents, commercially too, as long as you give credit: "Based on the AI App Policy Kit by PuglieseWeb LTD, https://www.puglieseweb.com/ai-policy-kit". Your own filled-in policies need no credit line.

## Who made this

[PuglieseWeb LTD](https://www.puglieseweb.com) makes software built with AI tools secure, reliable and ready to grow. If you would like someone to check your app against these documents, [book a free Software Health Check](https://www.puglieseweb.com/ai-policy-kit).

## Building the downloads

The Word and PDF files are built from `policies/*.md`:

```
pip install pypandoc_binary python-docx
python3 tools/build.py 1.0
```

It needs LibreOffice (`soffice`) for the PDFs and writes everything to `dist/`.
