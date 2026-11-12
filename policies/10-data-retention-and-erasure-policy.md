# 10. Data retention and erasure policy

> **Template.** Part of the open-source [AI App Policy Kit](https://www.puglieseweb.com/ai-policy-kit), version 1.0. Replace everything in [square brackets], delete what does not apply, and have the person who runs the business approve it. A starting point, not legal advice.

| | |
|---|---|
| **Business** | [Business name] |
| **Document owner** | [Name and role] |
| **Approved by, and date** | [Name], [date] |
| **Next review** | [Date, at most 12 months on] |

## Why this matters

UK GDPR says personal data is kept no longer than needed, and gives people the right to ask for theirs to be deleted. Apps built quickly usually keep everything for ever, in more places than anyone remembers: the database, backups, logs, analytics, the AI supplier's history, a spreadsheet export.

## Who it covers

All personal data held by [Business name], in every system in the data map (document 02).

## The rules

1. **Every kind of data has a retention period,** set in the schedule below, with the reason. "For ever" is not a period.
2. **Deletion is automatic where possible.** A scheduled job removes or anonymises records past their period. Where it is manual, it is in someone's calendar.
3. **Deletion means everywhere.** The database, file storage, search indexes, analytics, exports, the AI supplier's stored conversations and any knowledge base or vector store built from the data.
4. **Backups age out.** Data deleted from the live system leaves the backups when they expire, within [35] days. If a backup is restored, deletions made since are applied again from the log below.
5. **An erasure request is answered within one month.** Follow the steps below. Some data must be kept despite a request, for example invoices for tax: keep only that, and tell the person.
6. **Data used to train or fine-tune a model** is recorded, so you know which models contain whose data. If it cannot be removed from a model, do not put it in without a risk assessment (document 09).
7. **Old accounts are closed.** Accounts unused for [24] months are warned and then deleted.
8. **Test and development systems hold no real personal data,** or are covered by the same schedule.

## Retention schedule

| Data | Where it is | Kept for | Why | How it is deleted |
|---|---|---|---|---|
| Customer account details | [App database] | [Life of account + 12 months] | [Contract] | [Nightly job] |
| Invoices and payment records | [Accounts system] | [6 years after the tax year] | [Legal obligation] | [Yearly review] |
| AI conversations and prompts | [App database; AI supplier] | [90 days] | [Support and quality] | [Nightly job; supplier setting] |
| Application logs | [Logging service] | [30 to 90 days] | [Security] | [Automatic expiry] |
| Enquiries that did not become customers | [CRM] | [12 months] | [Legitimate interests] | [Quarterly review] |
| Job applications | [Email, documents] | [6 months after the decision] | [Legitimate interests] | [Manual] |
| Backups | [Backup store] | [35 days] | [Recovery] | [Automatic expiry] |

## Steps for an erasure request

1. Log the request and the date. Confirm who is asking, without collecting more data than needed.
2. Find their data in every system in the data map.
3. Decide what must be kept and why (legal duty, open dispute).
4. Delete or anonymise the rest, the AI supplier's copies included.
5. Tell any supplier or partner you shared it with.
6. Reply within one month: what was deleted, what was kept and why.
7. Record the completion date.

## Erasure log

Keep the least needed to prove the request was handled.

| Reference | Received | Systems cleared | Kept, and why | Replied on |
|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] |

## Checklist

- [ ] Every row of the data map has a row in the schedule.
- [ ] Deletion jobs ran in the last month, and someone checked.
- [ ] A test erasure was done end to end in the last 12 months, AI supplier included.
- [ ] Every request in the log was answered within one month.

## References

- ICO, *Storage limitation* and *Right to erasure*.

---

AI App Policy Kit, version 1.0. © 2026 PuglieseWeb LTD, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use it, change it and share it, with credit. The whole kit, and a free Software Health Check of your app against it: <https://www.puglieseweb.com/ai-policy-kit>
