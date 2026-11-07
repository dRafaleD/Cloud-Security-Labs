"""Static, offline container manifest audit. No Docker needed."""
manifest = {
    "image": "training-api:latest",
    "digest": None,
    "privileged": True,
    "run_as_non_root": False,
    "sbom": [{"name":"training-lib", "version":"1.0.0"}],
}
def audit(m):
    issues = []
    if not m.get("digest"): issues.append("image-not-digest-pinned")
    if m.get("privileged"): issues.append("privileged-runtime")
    if not m.get("run_as_non_root"): issues.append("root-runtime")
    if any(not d.get("version") for d in m.get("sbom", [])):
        issues.append("incomplete-sbom")
    return issues
issues = audit(manifest)
assert "privileged-runtime" in issues and "image-not-digest-pinned" in issues
print("Synthetic container findings:", issues)
