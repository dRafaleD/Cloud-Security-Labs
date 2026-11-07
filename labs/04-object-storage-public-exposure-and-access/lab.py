"""Offline storage exposure checks using synthetic objects."""
objects = {
    "catalog.jpg": {"sensitivity": "public", "public_grant": True},
    "backup.sql": {"sensitivity": "confidential", "public_grant": True},
}
block_public_access = True

def anonymous_read(name):
    item = objects[name]
    return not block_public_access and item["public_grant"]

def exposure_findings():
    return [name for name, obj in objects.items()
            if obj["public_grant"] and obj["sensitivity"] != "public"]

assert not anonymous_read("backup.sql")
assert exposure_findings() == ["backup.sql"]
print("Policy misconfiguration detected (blocked at account boundary):", exposure_findings())
