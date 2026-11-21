# Day 24 — Witness Membership Transitions and Rollback Guards

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lab.py)

## From Day 23
Day 23 enforced current witness membership and excluded signatures from stale epochs. Day 24 asks **how the trusted membership policy changes** without allowing a reader to roll it back or arbitrarily add a witness.

## Toy protocol
A membership proposal contains `from_epoch`, `to_epoch` and the exact new member set. Two **distinct currently active** fictional witnesses must produce valid HMAC tags for precisely that transition.

- **ROLLBACK_OR_REPLAY:** the proposed epoch is not newer.
- **SKIPPED_EPOCH:** a transition skips the next expected policy epoch.
- **INVALID_MEMBERSHIP:** unknown or insufficiently populated member set.
- **INSUFFICIENT_VOTES:** fewer than two distinct authenticated current members.
- **APPLIED:** the in-memory epoch and membership set change together.

The fixture also shows that forwarding the same vote twice does not create a quorum, and that a retired witness cannot approve the next change.

## Run
```bash
python3 labs/24-witness-membership-transitions-and-rollback-guards/lab.py
python3 test_all.py
```

## Questions
Why must the vote authenticate the entire membership set and policy epoch? Why shouldn't old-epoch votes approve the new policy? What happens if the trusted policy store is itself rolled back? Why is two-of-three HMAC approval not proof of distributed consensus?

## Limits
All keys and votes are made up. No cloud service, genuine certificates, tamper-proof storage, consensus or durability. Production membership governance needs independent trust anchors and audited policy changes.
