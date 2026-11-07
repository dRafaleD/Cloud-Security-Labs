"""Controls checklist, not encryption software."""
resources = [
    {"name":"backup-a", "tls":True, "encrypted_at_rest":True, "key_admin_only":False},
    {"name":"service-b", "tls":False, "encrypted_at_rest":True, "key_admin_only":True},
    {"name":"archive-c", "tls":True, "encrypted_at_rest":True, "key_admin_only":True},
]
def findings(item):
    result = []
    if not item["tls"]: result.append("transport-control-missing")
    if not item["encrypted_at_rest"]: result.append("storage-control-missing")
    if not item["key_admin_only"]: result.append("broad-key-access")
    return result
assert findings(resources[0]) == ["broad-key-access"]
assert findings(resources[1]) == ["transport-control-missing"]
assert not findings(resources[2])
for r in resources: print(r["name"], findings(r))
