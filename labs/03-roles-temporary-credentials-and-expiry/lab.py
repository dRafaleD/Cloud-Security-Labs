"""Offline temporary-session authorization; never creates actual tokens."""
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

@dataclass(frozen=True)
class Session:
    role: str
    issued_at: datetime
    expires_at: datetime
    actions: frozenset[str]

def permitted(session, now, action):
    return session.issued_at <= now < session.expires_at and action in session.actions

start = datetime(2026, 1, 1, tzinfo=timezone.utc)
session = Session("read-only", start, start + timedelta(minutes=10), frozenset({"read"}))
assert permitted(session, start + timedelta(minutes=9, seconds=59), "read")
assert not permitted(session, start + timedelta(minutes=10), "read")
assert not permitted(session, start + timedelta(minutes=2), "delete")
print("Temporary-role policy boundary checks passed.")
