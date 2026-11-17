# Day 20 — External Audit Checkpoints and Truncation Detection

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python exercise](lab.py)

## After Day 19
A hash chain can detect changes **if an expected digest is preserved outside the attacker's control**. Without an external anchor, an attacker can rewrite all records and recompute the entire chain—or delete the tail.

## Checkpoint model
A checkpoint stores `(event_count, final_chain_digest)` from a fictional four-event audit log. Imagine that the checkpoint was captured and preserved independently *before* a modification. Verification checks event sequence continuity, total count and computed final digest.

The fixed trusted checkpoint detects a rewritten event, removed final event, wrong count and reordered list. But the exercise deliberately proves that **if an attacker can replace the checkpoint too, the rewritten or truncated history verifies successfully**.

## Reproduce
~~~bash
python3 labs/20-external-audit-checkpoints-and-truncation-detection/lab.py
python3 test_all.py
~~~

## What real systems need
Independently anchored, access-controlled or signed checkpoints, reliable key management, timestamp validation, protected retention, log ingestion provenance, and documented consistency assumptions. A valid chain only supports integrity *relative to its anchor*, not truthfulness of the logged claims.

## Questions
1. Why doesn't a standalone final digest protect against a full rewrite?
2. Why must the checkpoint be stored under a separate trust boundary?
3. Can a checkpoint reveal an event that was never logged?
4. Why is an externally preserved count useful alongside the hash?
5. What would make cross-region audit records arrive out of order?

## Limits
Synthetic in-memory logs only. Checkpoints here are ordinary tuples, not signatures or secure distributed audit storage.
