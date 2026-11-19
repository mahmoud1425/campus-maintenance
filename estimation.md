# Estimation — Campus Maintenance Reporter

**Team 14 — Group 2 — Project #2: Campus Maintenance Reporter**

| Name | ID | Role |
|---|---|---|
| Mahmoud Mohamed | 192300395 | Product Owner |
| Ahmed Ehab Makram | 192300399 | Scrum Master |
| Mohamed Osama | 192300376 | Developer |
| Hisham Magdy | 192300419 | Developer |
| Mahmoud Ashour | 192300380 | Developer |

## Method
Planning Poker with the Fibonacci scale (1, 2, 3, 5, 8, 13). Each team member (PO, SM and the 3 developers) estimated privately, then we revealed together and discussed big gaps until we agreed. Points reflect **complexity + effort + uncertainty**, not hours.

## Reference stories (anchors)
- **2 pts (small):** US-04 Select location — a simple dropdown and one field.
- **3 pts (medium):** US-02 Submit report — form, validation, saving.
- **8 pts (large):** US-12 Admin dashboard — aggregation queries + charts + new UI.

All other stories were sized relative to these anchors.

## Estimates

| ID | Story | Points | Reasoning |
|---|---|---|---|
| US-01 | Campus email login | 3 | Auth setup, domain check |
| US-02 | Submit report | 3 | Form + DB + validation |
| US-03 | Attach photo | 3 | File upload + storage + preview |
| US-04 | Select location | 2 | Dropdown + field |
| US-05 | My reports list | 2 | Simple filtered query |
| US-06 | See status | 2 | Display field/badge |
| US-07 | Notifications | 5 | Email service, triggers, uncertainty |
| US-08 | Dispatcher list + filters | 5 | Multiple filters + sorting + pagination |
| US-09 | Assign technician | 3 | New relation + dropdown + status change |
| US-10 | Update status + comment | 3 | Status log + comments |
| US-11 | Set priority | 3 | New field + sorting + highlight |
| US-12 | Admin dashboard | 8 | Aggregations + charts |
| US-13 | Duplicate detection | 5 | Matching logic, edge cases |
| US-14 | Map view | 8 | Map library, pins, new unknown tech |
| US-15 | CSV export | 2 | Simple serialization |
| US-16 | Close rule + overdue flag | 3 | State-transition guard + 2-hour time rule (fake clock tests) |

**Total: 60 points · MVP: 32 points · Release 2: 28 points**

## Risks / Assumptions
- No story larger than 8 points; anything bigger should be split.
- US-14 and US-07 have the most uncertainty (new tech/services).
- US-16 depends on US-09, US-10 and US-11 (needs priority, assignment and status).
- Estimates will be revisited after Sprint 1 based on actual velocity.
