"""Synthetic audit checkpoints: detect conflicting histories at the same height."""
from dataclasses import dataclass
from hashlib import sha256
import json

@dataclass(frozen=True)
class Event:
    seq: int
    kind: str

PREFIX = [Event(1, "ISSUED"), Event(2, "ALLOWED")]
LEFT = PREFIX + [Event(3, "REVOKED"), Event(4, "DENIED")]
RIGHT = PREFIX + [Event(3, "STILL_ACTIVE"), Event(4, "ALLOWED")]
SHORT = PREFIX + [Event(3, "REVOKED")]

def checkpoint(events: list[Event]) -> tuple[int, str] | None:
    if any(e.seq != i for i, e in enumerate(events, 1)):
        return None
    state = "GENESIS"
    for e in events:
        raw = json.dumps({"seq": e.seq, "kind": e.kind},
                         sort_keys=True, separators=(",", ":"))
        state = sha256((state + "|" + raw).encode()).hexdigest()
    return len(events), state

def classify(a: tuple[int, str] | None,
             b: tuple[int, str] | None) -> str:
    if a is None or b is None:
        return "INVALID"
    if a[0] != b[0]:
        return "DIFFERENT_HEIGHTS"
    if a[1] == b[1]:
        return "CONSISTENT_AT_HEIGHT"
    return "CONFLICTING_CHECKPOINTS"

def main():
    a, b, c = checkpoint(LEFT), checkpoint(RIGHT), checkpoint(SHORT)
    assert a is not None and b is not None and c is not None
    checks = [
        ("self comparison", classify(a, a), "CONSISTENT_AT_HEIGHT"),
        ("same-height fork", classify(a, b), "CONFLICTING_CHECKPOINTS"),
        ("height differs", classify(a, c), "DIFFERENT_HEIGHTS"),
        ("identical copied log", classify(checkpoint(LEFT[:]), a), "CONSISTENT_AT_HEIGHT"),
        ("invalid sequence", classify(checkpoint([Event(2, "ISSUED")]), a), "INVALID"),
        ("different fork order", classify(b, a), "CONFLICTING_CHECKPOINTS"),
        ("no anchor", classify(None, a), "INVALID"),
    ]
    for name, actual, expected in checks:
        assert actual == expected, (name, actual)
        print(f"{name:24} {actual}")
    print("7/7 fictional audit-fork checks passed")

if __name__ == "__main__":
    main()
