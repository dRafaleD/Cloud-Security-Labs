"""Offline confused-deputy and external-ID teaching model; no cloud APIs."""
from dataclasses import dataclass

PARTNER_PRINCIPAL = "partner:reporting-service"  # assumed authenticated by caller
# Fictional references are NOT credentials or secrets.
EXPECTED_EXTERNAL_IDS = {
    "tenant-a": "reference-for-tenant-a",
    "tenant-b": "reference-for-tenant-b",
}
READABLE_REPORTS = {
    "tenant-a": "tenant-a/report:quarterly",
    "tenant-b": "tenant-b/report:quarterly",
}

@dataclass(frozen=True)
class AssumeRequest:
    principal: str
    tenant: str
    external_id: str

@dataclass(frozen=True)
class Session:
    principal: str
    tenant: str


def assume_role(request: AssumeRequest) -> Session | None:
    """Trust + tenant-specific external-ID condition, not permission grant."""
    expected = EXPECTED_EXTERNAL_IDS.get(request.tenant)
    if request.principal != PARTNER_PRINCIPAL or expected is None:
        return None
    if request.external_id != expected:
        return None
    return Session(principal=request.principal, tenant=request.tenant)


def access_report(session: Session | None, action: str, resource: str) -> bool:
    if session is None or action != "read":
        return False
    return READABLE_REPORTS.get(session.tenant) == resource


def main() -> None:
    cases = [
        ("correct tenant A", AssumeRequest(PARTNER_PRINCIPAL, "tenant-a", "reference-for-tenant-a"), "read", "tenant-a/report:quarterly", True),
        ("correct tenant B", AssumeRequest(PARTNER_PRINCIPAL, "tenant-b", "reference-for-tenant-b"), "read", "tenant-b/report:quarterly", True),
        ("wrong tenant reference", AssumeRequest(PARTNER_PRINCIPAL, "tenant-a", "reference-for-tenant-b"), "read", "tenant-a/report:quarterly", False),
        ("untrusted principal", AssumeRequest("guest:client", "tenant-a", "reference-for-tenant-a"), "read", "tenant-a/report:quarterly", False),
        ("cross-tenant access", AssumeRequest(PARTNER_PRINCIPAL, "tenant-a", "reference-for-tenant-a"), "read", "tenant-b/report:quarterly", False),
        ("unauthorized action", AssumeRequest(PARTNER_PRINCIPAL, "tenant-a", "reference-for-tenant-a"), "delete", "tenant-a/report:quarterly", False),
        ("unknown tenant", AssumeRequest(PARTNER_PRINCIPAL, "tenant-x", "reference-for-tenant-a"), "read", "tenant-a/report:quarterly", False),
    ]
    for label, request, action, resource, expected in cases:
        result = access_report(assume_role(request), action, resource)
        assert result is expected, label
        print(f"{label:24} {'ALLOW' if result else 'DENY'}")
    print("7/7 synthetic confused-deputy cases passed; no cloud calls made.")

if __name__ == "__main__":
    main()
