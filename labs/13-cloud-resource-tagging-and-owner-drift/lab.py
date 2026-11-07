"""Offline cloud inventory drift review; no cloud API calls."""
baseline={
 "api-01":{"owner":"backend","environment":"production"},
 "sandbox-01":{"owner":"students","environment":"test"},
}
observed={
 "api-01":{"owner":"","environment":"production"},
 "sandbox-01":{"owner":"students","environment":"production"},
}
findings=[]
for asset,old in baseline.items():
    new=observed.get(asset)
    if new is None:
        findings.append((asset,"missing-resource"))
        continue
    if not new.get("owner"):
        findings.append((asset,"missing-owner"))
    if new.get("environment") != old.get("environment"):
        findings.append((asset,"environment-drift"))
assert findings == [
 ("api-01","missing-owner"),
 ("sandbox-01","environment-drift")]
print("Review candidates (not proof of compromise):",findings)
