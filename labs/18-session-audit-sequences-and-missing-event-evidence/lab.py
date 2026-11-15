"""Offline model of sequence gaps in a fictional cloud session audit trail."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Event:
    seq: int
    session: str
    kind: str

COMPLETE = [
    Event(1, "s-1", "ISSUED"),
    Event(2, "s-1", "ALLOWED_WHILE_ACTIVE"),
    Event(3, "s-1", "REVOKED"),
    Event(4, "s-1", "DENIED_REVOKED"),
]

def validate(events: list[Event]) -> tuple[bool, str]:
    active = set()
    for expected_seq, event in enumerate(events, start=1):
        if event.seq != expected_seq:
            return False, "sequence gap, duplicate or reordering"
        if event.kind == "ISSUED":
            if event.session in active:
                return False, "duplicate issuance"
            active.add(event.session)
        elif event.kind == "ALLOWED_WHILE_ACTIVE":
            if event.session not in active:
                return False, "allow without active session"
        elif event.kind == "REVOKED":
            if event.session not in active:
                return False, "revoke without active session"
            active.remove(event.session)
        elif event.kind == "DENIED_REVOKED":
            if event.session in active:
                return False, "denial contradicts simple revoked-only model"
        else:
            return False, "unknown event kind"
    return True, "internally consistent toy trace"

def main():
    cases = [
        ("complete", COMPLETE, True),
        ("missing revocation", [COMPLETE[0], COMPLETE[1], COMPLETE[3]], False),
        ("duplicate sequence", [COMPLETE[0], COMPLETE[0]], False),
        ("reordered", [COMPLETE[1], COMPLETE[0]], False),
        ("allow after revocation", COMPLETE + [Event(5, "s-1", "ALLOWED_WHILE_ACTIVE")], False),
        ("unknown event", [Event(1, "s-1", "UNKNOWN")], False),
        ("revoke without issue", [Event(1, "s-1", "REVOKED")], False),
        ("unrelated session allow", [Event(1, "s-2", "ALLOWED_WHILE_ACTIVE")], False),
    ]
    for label, events, expected in cases:
        valid, reason = validate(events)
        assert valid is expected, (label, reason)
        print(f"{label:25} {reason}")
    print("8/8 synthetic sequence checks passed; no tamper-proof guarantee")

if __name__ == "__main__":
    main()
