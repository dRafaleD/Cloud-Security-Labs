"""Offline audit hash-chain checkpoint model; no cloud APIs or real log storage."""
from dataclasses import dataclass
from hashlib import sha256
import json

@dataclass(frozen=True)
class Event:
    seq: int
    kind: str

EVENTS = [
    Event(1, "ISSUED"),
    Event(2, "ALLOWED"),
    Event(3, "REVOKED"),
    Event(4, "DENIED"),
]

def chain(events: list[Event]) -> str:
    previous = "GENESIS"
    for event in events:
        body = json.dumps({"seq": event.seq, "kind": event.kind},
                          sort_keys=True, separators=(",", ":"))
        previous = sha256((previous + "|" + body).encode()).hexdigest()
    return previous

def checkpoint(events: list[Event]) -> tuple[int, str]:
    return len(events), chain(events)

def validate(events: list[Event], trusted: tuple[int, str]) -> bool:
    if any(event.seq != index for index, event in enumerate(events, 1)):
        return False
    return checkpoint(events) == trusted

def main() -> None:
    # Imagine this checkpoint was independently retained BEFORE log alteration.
    trusted = checkpoint(EVENTS)
    rewritten = [*EVENTS[:2], Event(3, "REMOVED_IN_REWRITE"), EVENTS[3]]
    truncated = EVENTS[:-1]
    reordered = [EVENTS[0], EVENTS[2], EVENTS[1], EVENTS[3]]
    checks = [
        ("original matches anchor", validate(EVENTS, trusted)),
        ("rewritten chain fails old anchor", not validate(rewritten, trusted)),
        ("truncated tail fails old anchor", not validate(truncated, trusted)),
        ("reordered fails", not validate(reordered, trusted)),
        ("empty history fails", not validate([], trusted)),
        ("tampered anchor can be forged", validate(rewritten, checkpoint(rewritten))),
        ("truncated anchor can be forged", validate(truncated, checkpoint(truncated))),
        ("wrong digest fails", not validate(EVENTS, (4, "0" * 64))),
        ("wrong count fails", not validate(EVENTS, (5, trusted[1]))),
    ]
    for label, passed in checks:
        assert passed, label
        print(f"{label:33} PASS")
    print("9/9 synthetic checkpoint checks passed")
    print("An untrusted checkpoint is NOT a security anchor.")

if __name__ == "__main__":
    main()
