"""Offline shared-responsibility example; illustrative, not provider policy."""
responsibilities = {
    "IaaS": {"physical": "provider", "guest_os": "customer", "iam": "customer", "data": "customer"},
    "PaaS": {"physical": "provider", "guest_os": "provider", "iam": "customer", "data": "customer"},
    "SaaS": {"physical": "provider", "guest_os": "provider", "iam": "shared", "data": "customer"},
}
assets = [
    {"id": "training-db-01", "kind": "database", "owner": "backend-team", "classification": "internal"},
    {"id": "training-web-01", "kind": "web-app", "owner": "app-team", "classification": "public"},
]
for model, controls in responsibilities.items():
    print(model, controls)
assert responsibilities["IaaS"]["guest_os"] == "customer"
assert responsibilities["PaaS"]["iam"] == "customer"
assert all(asset["owner"] and asset["classification"] for asset in assets)
print("Asset inventory:", assets)
