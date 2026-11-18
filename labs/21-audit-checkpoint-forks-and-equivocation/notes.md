# Day 21 — Audit Checkpoint Forks and Equivocation

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lab.py)

## From Day 20
An independently retained `(event count, final hash)` checkpoint helps reveal rewritten or truncated logs. But what if a logging service supplies **different histories of the same length to different reviewers**?

## Fork detection
Two fictional trails start with the same issuance/allow records, then branch into contradictory revocation/allow outcomes. Their final checkpoints have the same event count but different digests.

- **CONSISTENT_AT_HEIGHT:** same count and same digest, subject to assumptions about the hash function and trusted origins.
- **CONFLICTING_CHECKPOINTS:** same count but different digests; strong evidence of differing data, not a verdict about which history is true.
- **DIFFERENT_HEIGHTS:** ordinary differences in progress can exist; cannot conclude equivocation from length alone.
- **INVALID:** a checkpoint cannot be computed or supplied.

This illustrates **equivocation / split view**, where different verifiers may see different versions of an append-only history. Independent comparison between authenticated checkpoints is necessary; if an attacker controls all checkpoints, detection is not guaranteed.

## Reproduce
~~~bash
python3 labs/21-audit-checkpoint-forks-and-equivocation/lab.py
python3 test_all.py
~~~

## Questions
1. Why can equal-length logs still disagree?
2. Why does a different final hash not identify the dishonest source by itself?
3. How could independent witnesses or auditors compare signed checkpoints?
4. Why does this toy hash comparison fail to prove event authenticity?
5. What changes when one checkpoint is simply newer?

## Limits
No real cloud, keys, signatures, witness protocols or production transparency log. Entirely deterministic synthetic records.
