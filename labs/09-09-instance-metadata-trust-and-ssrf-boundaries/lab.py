"""Toy metadata-token policy. No HTTP calls, metadata IPs or cloud credentials."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Token:
    value: str
    expiry_second: int

def metadata_allowed(token, supplied, now):
    return (token is not None and supplied is not None and
            token.value == supplied and now < token.expiry_second)

t = Token("demo-token-not-a-secret", 120)
assert metadata_allowed(t, "demo-token-not-a-secret", 119)
assert not metadata_allowed(t, None, 119)
assert not metadata_allowed(t, "wrong", 119)
assert not metadata_allowed(t, t.value, 120)
print("Synthetic metadata gate checks passed. No requests were sent.")
