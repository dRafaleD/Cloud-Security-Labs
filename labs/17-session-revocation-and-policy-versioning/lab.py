"""Synthetic cloud-session revocation and policy-version checks; no cloud APIs."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Session:
    session_id: str
    tenant: str
    action: str
    resource: str
    issued_at: int
    expires_at: int
    policy_version: int

CURRENT_POLICY_VERSION = {"tenant-a": 1}
REVOKED: set[str] = set()

def authorize(session: Session | None, tenant: str, action: str,
              resource: str, now: int) -> bool:
    if session is None or session.session_id in REVOKED:
        return False
    return (
        session.tenant == tenant
        and session.action == action
        and session.resource == resource
        and session.issued_at <= now < session.expires_at
        and session.policy_version == CURRENT_POLICY_VERSION.get(tenant)
    )

def main():
    s = Session("toy-session-1", "tenant-a", "read", "report-a", 100, 160, 1)
    assert authorize(s, "tenant-a", "read", "report-a", 100)
    assert authorize(s, "tenant-a", "read", "report-a", 159)
    assert not authorize(s, "tenant-a", "read", "report-a", 160)
    assert not authorize(s, "tenant-b", "read", "report-a", 120)
    assert not authorize(s, "tenant-a", "write", "report-a", 120)
    assert not authorize(s, "tenant-a", "read", "report-b", 120)
    CURRENT_POLICY_VERSION["tenant-a"] = 2
    assert not authorize(s, "tenant-a", "read", "report-a", 120)
    newer = Session("toy-session-2", "tenant-a", "read", "report-a", 120, 180, 2)
    assert authorize(newer, "tenant-a", "read", "report-a", 130)
    REVOKED.add("toy-session-2")
    assert not authorize(newer, "tenant-a", "read", "report-a", 130)
    assert not authorize(None, "tenant-a", "read", "report-a", 130)
    print("10/10 synthetic revocation and policy-version checks passed")

if __name__ == "__main__":
    main()
