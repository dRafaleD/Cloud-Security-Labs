# Day 19 — Audit Hash Chains and Integrity Limits

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python practice](lab.py)

## Connection to Day 18
Day 18 used sequence numbers to flag missing or reordered cloud-session events. Day 19 adds a **hash chain**, where each record's SHA-256 depends on its contents **and the preceding record's digest**.

## How it works
For a fictional `ISSUED → ALLOWED → REVOKED → DENIED` audit trail, each row stores:
- the structured event;
- the previous row's digest (or a genesis anchor);
- `SHA256(previous_digest || "|" || canonical_event)`.

Verification checks consecutive sequence numbers, the previous-hash link and each computed digest. A changed middle record, removed record or reordered list fails **if subsequent hashes remain fixed**.

## Critical limitations
A hash chain is **not a signature**, tamper-proof storage or a guarantee of completeness. The script also demonstrates two cases that **still validate**:
1. A malicious editor rewrites the record and recomputes **the entire chain**.
2. The last event is deleted and no externally retained final checkpoint exists.

Real integrity claims require trusted timestamps, access-controlled ingestion, independently anchored checkpoints or signed log roots, key management, retention and collection provenance. For distributed services, event-order guarantees must be justified separately.

## Run
~~~bash
python3 labs/19-audit-hash-chains-and-integrity-limits/lab.py
python3 test_all.py
~~~

## Questions
1. How does a hash chain differ from a standalone per-event hash?
2. Why does rebuilding a chain defeat its unauthenticated integrity check?
3. Why might deleting the final row go undetected?
4. What should be stored externally to detect a rewritten or truncated history?
5. Can a cryptographically valid record prove that the original event was true?

## Scope
No cloud services, real credentials or logs. The example teaches evidence limitations, not production audit security.
