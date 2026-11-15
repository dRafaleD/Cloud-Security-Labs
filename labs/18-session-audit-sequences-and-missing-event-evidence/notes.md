# Day 18 — Session Audit Sequences and Missing-Event Evidence

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python practice](lab.py)

## Connection to Day 17
Revoking a session is only part of the story: **what evidence can an investigator examine afterward?** An audit trace may contain issuance, allowed actions, revocation and denied actions. Missing or reordered records reduce confidence.

## Toy model
The exercise uses fictional sequential records `ISSUED → ALLOWED_WHILE_ACTIVE → REVOKED → DENIED_REVOKED`. It checks:
- strict sequence-number continuity;
- issuance before allowed actions;
- revocation only of an active session;
- no allowed action after that session has been revoked;
- explicit rejection of unknown event kinds.

A removed revocation record creates a **sequence gap**. However, an attacker who rewrites every sequence number could hide the gap. These assertions do not authenticate producers, prevent deletion or prove cryptographic integrity. Real audit evidence requires access controls, secure timestamps, independent retention, provenance and validation of logging gaps.

## Reproduce
~~~bash
python3 labs/18-session-audit-sequences-and-missing-event-evidence/lab.py
python3 test_all.py
~~~

## Questions
1. Why does a sequence gap indicate missing records but not their cause?
2. What cannot be proved by an internally consistent event sequence?
3. How can distributed cloud services create legitimate reordering?
4. Why must an investigator preserve original raw events?

## Limits
No cloud credentials, APIs or real logs. This is a constrained **revoked-only** model of denial, not a general IAM audit validator.
