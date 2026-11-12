"""Offline cloud session lifetime and permission-scope teaching model."""
from dataclasses import dataclass

PARTNER = "partner:reporting-service"
TENANTS = {
    "tenant-a": {"external_id": "toy-ref-a", "report": "tenant-a/report:summary"},
    "tenant-b": {"external_id": "toy-ref-b", "report": "tenant-b/report:summary"},
}

@dataclass(frozen=True)
class Session:
    principal: str
    tenant: str
    resource: str
    allowed_actions: frozenset[str]
    issued_at: int
    expires_at: int

def issue(principal: str, tenant: str, external_id: str,
          now: int, ttl: int) -> Session | None:
    config = TENANTS.get(tenant)
    if principal != PARTNER or config is None:
        return None
    if external_id != config["external_id"] or not 1 <= ttl <= 3600:
        return None
    return Session(principal, tenant, config["report"],
                   frozenset({"read"}), now, now + ttl)

def authorize(session: Session | None, principal: str, tenant: str,
              action: str, resource: str, now: int) -> bool:
    if session is None:
        return False
    return (principal == session.principal
            and tenant == session.tenant
            and session.issued_at <= now < session.expires_at
            and action in session.allowed_actions
            and resource == session.resource)

def main() -> None:
    session = issue(PARTNER, "tenant-a", "toy-ref-a", now=100, ttl=60)
    assert session is not None
    resource = TENANTS["tenant-a"]["report"]
    checks = [
        ("start boundary", session, PARTNER, "tenant-a", "read", resource, 100, True),
        ("before expiry", session, PARTNER, "tenant-a", "read", resource, 159, True),
        ("at expiry", session, PARTNER, "tenant-a", "read", resource, 160, False),
        ("before issue", session, PARTNER, "tenant-a", "read", resource, 99, False),
        ("write denied", session, PARTNER, "tenant-a", "write", resource, 120, False),
        ("cross tenant", session, PARTNER, "tenant-b", "read", resource, 120, False),
        ("other resource", session, PARTNER, "tenant-a", "read", TENANTS["tenant-b"]["report"], 120, False),
        ("other principal", session, "guest", "tenant-a", "read", resource, 120, False),
    ]
    for label, s, principal, tenant, action, target, clock, expected in checks:
        actual = authorize(s, principal, tenant, action, target, clock)
        assert actual is expected, label
        print(f"{label:19} {'ALLOW' if actual else 'DENY'}")
    assert issue(PARTNER, "tenant-a", "toy-ref-b", 100, 60) is None
    assert issue(PARTNER, "tenant-a", "toy-ref-a", 100, 0) is None
    print("10/10 synthetic session checks passed; no cloud calls or real credentials.")

if __name__ == "__main__":
    main()
