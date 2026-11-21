"""Synthetic audit-witness membership changes with anti-rollback checks."""
from hashlib import sha256
import hmac
import json

KEYS = {"a": b"fictional-a", "b": b"fictional-b", "c": b"fictional-c"}
STATE = {"epoch": 1, "active": {"a", "b", "c"}}

def payload(signer: str, old_epoch: int, new_epoch: int,
            new_members: set[str]) -> bytes:
    fields = {"signer": signer, "from": old_epoch, "to": new_epoch,
              "members": sorted(new_members)}
    return json.dumps(fields, sort_keys=True, separators=(",", ":")).encode()

def sign(signer: str, old_epoch: int, new_epoch: int,
         new_members: set[str]) -> str:
    return hmac.new(KEYS[signer],
                    payload(signer, old_epoch, new_epoch, new_members),
                    sha256).hexdigest()

def change(new_epoch: int, members: set[str],
           votes: list[tuple[str, str]]) -> str:
    if type(new_epoch) is not int:
        return "INVALID_EPOCH"
    if new_epoch <= STATE["epoch"]:
        return "ROLLBACK_OR_REPLAY"
    if new_epoch != STATE["epoch"] + 1:
        return "SKIPPED_EPOCH"
    if len(members) < 2 or not members <= KEYS.keys():
        return "INVALID_MEMBERSHIP"
    accepted = set()
    for signer, tag in votes:
        if signer not in STATE["active"] or not isinstance(tag, str):
            continue
        expected = sign(signer, STATE["epoch"], new_epoch, members)
        if hmac.compare_digest(tag, expected):
            accepted.add(signer)
    if len(accepted) < 2:
        return "INSUFFICIENT_VOTES"
    # Illustrates one logical state transition. Not durable or distributed.
    STATE["epoch"] = new_epoch
    STATE["active"] = set(members)
    return "APPLIED"

def ballots(members: set[str], old: int, new: int,
            signers: list[str]) -> list[tuple[str, str]]:
    return [(s, sign(s, old, new, members)) for s in signers]

def main() -> None:
    next_members = {"b", "c"}
    votes = ballots(next_members, 1, 2, ["a", "b"])
    checks = [
        ("replay current epoch", change(1, next_members, votes), "ROLLBACK_OR_REPLAY"),
        ("skip an epoch", change(3, next_members, votes), "SKIPPED_EPOCH"),
        ("unknown new member", change(2, {"b", "unknown"}, votes), "INVALID_MEMBERSHIP"),
        ("one approver", change(2, next_members, votes[:1]), "INSUFFICIENT_VOTES"),
        ("copied vote", change(2, next_members, [votes[0], votes[0]]), "INSUFFICIENT_VOTES"),
        ("tampered tag", change(2, next_members, [(votes[0][0], "0"*64), votes[1]]), "INSUFFICIENT_VOTES"),
        ("two active approvals", change(2, next_members, votes), "APPLIED"),
        ("old epoch proposal again", change(2, next_members, votes), "ROLLBACK_OR_REPLAY"),
    ]
    future_members = {"a", "c"}
    stale = ballots(future_members, 2, 3, ["a", "b"])
    checks.append(("retired signer cannot count",
                   change(3, future_members, stale), "INSUFFICIENT_VOTES"))
    fresh = ballots(future_members, 2, 3, ["b", "c"])
    checks.append(("current witnesses approve next",
                   change(3, future_members, fresh), "APPLIED"))
    for title, actual, expected in checks:
        assert actual == expected, (title, actual)
        print(f"{title:37} {actual}")
    assert STATE == {"epoch": 3, "active": {"a", "c"}}
    print(f"{len(checks)+1}/{len(checks)+1} membership-transition checks passed")

if __name__ == "__main__":
    main()
