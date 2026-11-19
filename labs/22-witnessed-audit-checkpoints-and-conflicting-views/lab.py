"""Fictional audit-checkpoint witnesses; HMAC is not a production signature."""
from dataclasses import dataclass
import hashlib
import hmac
import json

KEYS = {
    "witness-a": b"fictional-a",
    "witness-b": b"fictional-b",
    "witness-c": b"fictional-c",
}
@dataclass(frozen=True)
class Checkpoint:
    height: int
    digest: str

@dataclass(frozen=True)
class Attestation:
    witness: str
    checkpoint: Checkpoint
    tag: str

A = Checkpoint(4, "a" * 64)
B = Checkpoint(4, "b" * 64)
NEWER = Checkpoint(5, "c" * 64)

def tag(witness: str, cp: Checkpoint, key: bytes) -> str:
    body = json.dumps({"witness": witness, "height": cp.height,
                       "digest": cp.digest}, sort_keys=True,
                      separators=(",", ":")).encode()
    return hmac.new(key, body, hashlib.sha256).hexdigest()

def sign(witness: str, cp: Checkpoint) -> Attestation:
    return Attestation(witness, cp, tag(witness, cp, KEYS[witness]))

def valid(a: Attestation) -> bool:
    key = KEYS.get(a.witness)
    if key is None or not isinstance(a.tag, str):
        return False
    if type(a.checkpoint.height) is not int or a.checkpoint.height < 0:
        return False
    return hmac.compare_digest(a.tag, tag(a.witness, a.checkpoint, key))

def assess(records: list[Attestation], quorum: int = 2) -> str:
    accepted = [a for a in records if valid(a)]
    if not accepted:
        return "INSUFFICIENT"
    heights = {a.checkpoint.height for a in accepted}
    if len(heights) > 1:
        return "MIXED_HEIGHTS"
    by_witness: dict[str, set[str]] = {}
    by_digest: dict[str, set[str]] = {}
    for a in accepted:
        by_witness.setdefault(a.witness, set()).add(a.checkpoint.digest)
        by_digest.setdefault(a.checkpoint.digest, set()).add(a.witness)
    if any(len(digests) > 1 for digests in by_witness.values()):
        return "WITNESS_EQUIVOCATION"
    if len(by_digest) > 1:
        return "CONFLICTING_VIEWS"
    return "QUORUM" if len(next(iter(by_digest.values()))) >= quorum else "INSUFFICIENT"

def main():
    checks = [
        ("two witnesses", [sign("witness-a", A), sign("witness-b", A)], "QUORUM"),
        ("three witnesses", [sign(w, A) for w in KEYS], "QUORUM"),
        ("one witness", [sign("witness-a", A)], "INSUFFICIENT"),
        ("copied attestation", [sign("witness-a", A)] * 2, "INSUFFICIENT"),
        ("two different views", [sign("witness-a", A), sign("witness-b", B)], "CONFLICTING_VIEWS"),
        ("witness double signs", [sign("witness-a", A), sign("witness-a", B)], "WITNESS_EQUIVOCATION"),
        ("majority plus fork", [sign("witness-a", A), sign("witness-b", A), sign("witness-c", B)], "CONFLICTING_VIEWS"),
        ("mixed heights", [sign("witness-a", A), sign("witness-b", NEWER)], "MIXED_HEIGHTS"),
        ("forged tag", [sign("witness-a", A), Attestation("witness-b", A, "0"*64)], "INSUFFICIENT"),
        ("empty", [], "INSUFFICIENT"),
    ]
    for title, records, expected in checks:
        result = assess(records)
        assert result == expected, (title, result)
        print(f"{title:26} {result}")
    print(f"{len(checks)}/{len(checks)} synthetic witness checks passed")

if __name__ == "__main__":
    main()
