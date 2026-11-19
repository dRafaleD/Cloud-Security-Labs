# Day 22 — Witnessed Audit Checkpoints and Conflicting Views

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lab.py)

## Day 21 follow-up
Day 21 showed that two observers can receive conflicting final audit-log hashes at the **same event count**. Day 22 adds fictional **independent witnesses** that endorse a checkpoint `(height, digest)`.

## Model
Three demonstration witnesses each hold a separate toy HMAC key. Their attestations bind their identity, checkpoint height and hash. A checkpoint reaches a **2-of-3 quorum** only when two distinct trusted witness IDs support the same height and digest.

The classifier also flags:
- **CONFLICTING_VIEWS** when different valid digests are observed at the same height, even if one has a majority.
- **WITNESS_EQUIVOCATION** when one witness signs contradictory digests at the same height.
- **MIXED_HEIGHTS** when checkpoints concern different lengths and cannot be compared as an equal-height fork.
- **INSUFFICIENT** when there are too few distinct valid witnesses.

An identical forwarded attestation does **not** count as a second witness.

## Run
```bash
python3 labs/22-witnessed-audit-checkpoints-and-conflicting-views/lab.py
python3 test_all.py
```

## Questions
1. Why is copying a witness attestation not additional independent approval?
2. How is an equal-height fork different from a newer checkpoint?
3. Why should a minority conflicting view be investigated rather than silently ignored?
4. Can a compromised witness key create valid-looking attestations?
5. What additional guarantees would actual signed, anchored transparency logs require?

## Limits
All keys and digest values are fictional. HMAC is symmetric and this is not a real multi-party log protocol, cloud service or cryptographic transparency system.
