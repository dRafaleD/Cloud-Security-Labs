"""Tiny offline IAM evaluator; NOT an AWS/Azure/GCP policy interpreter."""
rules = [
    {"effect": "allow", "principal": "reporter", "action": "read", "resource": "dataset:weekly"},
    {"effect": "deny", "principal": "reporter", "action": "delete", "resource": "dataset:weekly"},
]
def authorize(principal, action, resource):
    matching = [r for r in rules if (r["principal"], r["action"], r["resource"]) == (principal, action, resource)]
    if any(r["effect"] == "deny" for r in matching):
        return False
    return any(r["effect"] == "allow" for r in matching)
cases = [
    ("reporter", "read", "dataset:weekly", True),
    ("reporter", "delete", "dataset:weekly", False),
    ("reporter", "read", "dataset:private", False),
    ("visitor", "read", "dataset:weekly", False),
]
for p, a, r, expected in cases:
    decision = authorize(p, a, r)
    print(p, a, r, "ALLOW" if decision else "DENY")
    assert decision is expected
