"""Cloud IR capstone: synthetic audit events, no credentials or network access."""
from datetime import datetime, timezone

events = [
 {"id":"c2","time":"2026-04-09T10:03:00Z","actor":"service-a","kind":"policy_change","resource":"bucket:archive","source":"198.51.100.9"},
 {"id":"c1","time":"2026-04-09T10:00:00Z","actor":"service-a","kind":"login_success","resource":"identity:service-a","source":"198.51.100.9"},
 {"id":"c3","time":"2026-04-09T10:04:00Z","actor":"service-a","kind":"object_read","resource":"bucket:archive","source":"198.51.100.9"},
]
def ts(e):
    return datetime.fromisoformat(e["time"].replace("Z","+00:00")).astimezone(timezone.utc)
events.sort(key=lambda e: (ts(e), e["id"]))
assert [e["id"] for e in events] == ["c1","c2","c3"]
report = {
 "direct_observations": [e["id"] + ": " + e["kind"] for e in events],
 "hypothesis": "Possible unexpected policy change; intent unknown.",
 "missing_evidence": ["change approval", "session context", "resource access baseline"],
 "confirmed_compromise": False,
}
assert report["confirmed_compromise"] is False
for key, value in report.items(): print(key, ":", value)
