# Day 23 — Witness Membership Epochs and Checkpoint Quorum

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](lab.py)

## From Day 22
Two matching endorsements from different witnesses formed a quorum for a fictional audit checkpoint. Day 23 introduces **membership change**: what if a witness is retired or its authentication key is no longer trusted?

## Model
Attestations bind witness ID, **membership epoch**, event-count height and checkpoint hash with toy HMAC. The controller stores the current epoch and active witness set. After rotation from epoch 1 `{a,b,c}` to epoch 2 `{b,c}`, the old witness A and **all epoch-1 endorsements** stop contributing to quorum. Only two distinct valid current-epoch witnesses may establish `QUORUM`.

Conflicting current views remain `CONFLICTING_VIEWS`; duplicate forwarded attestations count once.

## Run
```bash
python3 labs/23-witness-membership-epochs-and-checkpoint-quorum/lab.py
python3 test_all.py
```

## Questions
1. Why must witness membership have a separately trusted policy version?
2. Why should old endorsements not count toward a new membership quorum?
3. How does witness key compromise affect a verified HMAC?
4. Why can two witnesses share an upstream source despite different identities?
5. What authenticated consensus or public signatures would a real transparency log need?

## Limits
Single-process toy simulation, hardcoded keys, no actual cloud provider or distributed consensus. Membership updates have no persistence or crash safety.
