"""Offline hash-chained audit records: detect edits, explain missing trust anchors."""
from hashlib import sha256
import json

GENESIS = sha256(b"fictional training anchor").hexdigest()
EVENTS = [
    {"seq": 1, "session": "toy-s1", "kind": "ISSUED"},
    {"seq": 2, "session": "toy-s1", "kind": "ALLOWED"},
    {"seq": 3, "session": "toy-s1", "kind": "REVOKED"},
    {"seq": 4, "session": "toy-s1", "kind": "DENIED"},
]

def digest(previous: str, event: dict) -> str:
    encoded = json.dumps(event, sort_keys=True, separators=(",", ":")).encode()
    return sha256(previous.encode() + b"|" + encoded).hexdigest()

def chain(events: list[dict]) -> list[dict]:
    previous = GENESIS
    result = []
    for event in events:
        current = digest(previous, event)
        result.append({"event": dict(event), "previous": previous, "hash": current})
        previous = current
    return result

def verify(records: list[dict], anchor: str = GENESIS) -> bool:
    if not records:
        return False
    previous = anchor
    for expected_seq, row in enumerate(records, start=1):
        event = row.get("event", {})
        if event.get("seq") != expected_seq:
            return False
        if row.get("previous") != previous:
            return False
        if row.get("hash") != digest(previous, event):
            return False
        previous = row["hash"]
    return True

def main() -> None:
    clean = chain(EVENTS)
    modified = chain(EVENTS)
    modified[1]["event"]["kind"] = "DENIED"  # hash not updated
    removed = clean[:1] + clean[2:]
    reordered = [clean[1], clean[0], *clean[2:]]
    rewrite = [dict(event) for event in EVENTS]
    rewrite[1]["kind"] = "DENIED"
    cases = [
        ("original", verify(clean), True),
        ("edited without rehash", verify(modified), False),
        ("missing middle record", verify(removed), False),
        ("reordered records", verify(reordered), False),
        ("different anchor", verify(clean, "incorrect-anchor"), False),
        ("fully rewritten and rehashed", verify(chain(rewrite)), True),
        ("truncated end without checkpoint", verify(clean[:-1]), True),
    ]
    for label, result, expected in cases:
        assert result is expected, label
        print(f"{label:39} {'VALID' if result else 'INVALID'}")
    print("7/7 synthetic audit checks passed")
    print("Hash chains alone DO NOT prove authenticity or completeness.")

if __name__ == "__main__":
    main()
