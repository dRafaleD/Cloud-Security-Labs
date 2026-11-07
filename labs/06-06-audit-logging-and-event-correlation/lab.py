"""Synthetic cloud audit timeline; no provider account access."""
from datetime import datetime, timezone

events = [
 {"id":"e3","at":"2026-02-01T12:05:00Z","actor":"ops","event":"policy_change","resource":"storage:demo"},
 {"id":"e1","at":"2026-02-01T12:00:00Z","actor":"ops","event":"login_failure","resource":"identity:ops"},
 {"id":"e2","at":"2026-02-01T12:01:00Z","actor":"ops","event":"login_success","resource":"identity:ops"},
]
def parse(s):
    return datetime.fromisoformat(s.replace("Z","+00:00")).astimezone(timezone.utc)
timeline = sorted(events, key=lambda e:(parse(e["at"]),e["id"]))
assert [e["id"] for e in timeline] == ["e1","e2","e3"]
for event in timeline:
    print(event["at"], event["actor"], event["event"], event["resource"])
print("Ordering is observed; intent and compromise are not established.")
