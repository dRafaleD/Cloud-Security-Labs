"""Cross-account role policy example. No cloud account or network access."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Request:
    principal: str
    action: str
    resource: str

# Fictional identities/resources: NOT a cloud-provider IAM policy format.
TRUSTED = {"tenant-a:reporter"}
PERMISSIONS = {("read", "report:quarterly")}

def authorize_role_request(request: Request) -> bool:
    trusted_assumption = request.principal in TRUSTED
    permitted_action = (request.action, request.resource) in PERMISSIONS
    return trusted_assumption and permitted_action

cases = [
    (Request("tenant-a:reporter", "read", "report:quarterly"), True),
    (Request("tenant-b:guest", "read", "report:quarterly"), False),
    (Request("tenant-a:reporter", "delete", "report:quarterly"), False),
    (Request("tenant-a:reporter", "read", "report:private"), False),
    (Request("tenant-b:guest", "delete", "report:private"), False),
]
for request, expected in cases:
    actual = authorize_role_request(request)
    assert actual is expected
    print(request, "->", "ALLOW" if actual else "DENY")

assert len(cases) == 5
print("5/5 trust-and-permission composition cases passed.")
