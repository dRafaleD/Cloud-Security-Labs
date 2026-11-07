"""Offline IaC-shaped configuration checks. Makes no cloud changes."""
config = {
    "audit_logging": False,
    "ingress": [{"port":22, "source":"0.0.0.0/0"},
                {"port":443, "source":"10.0.0.0/8"}],
    "storage": {"public":False, "encrypted":True},
}
def lint(c):
    findings = []
    if not c.get("audit_logging"): findings.append("audit-logging-disabled")
    if any(r["port"] == 22 and r["source"] == "0.0.0.0/0" for r in c["ingress"]):
        findings.append("ssh-open-to-internet")
    if c["storage"]["public"]: findings.append("storage-public")
    if not c["storage"]["encrypted"]: findings.append("storage-not-encrypted")
    return findings
assert lint(config) == ["audit-logging-disabled", "ssh-open-to-internet"]
print("Pre-deployment findings:", lint(config))
