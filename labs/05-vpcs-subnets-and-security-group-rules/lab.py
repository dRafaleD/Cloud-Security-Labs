"""Offline source-CIDR + destination-port check. No packets sent."""
from ipaddress import ip_address, ip_network

allow_rules = [{"source": ip_network("10.1.0.0/16"), "port": 443, "protocol": "tcp"}]
def allows(source, port, protocol="tcp"):
    return any(ip_address(source) in r["source"] and
               port == r["port"] and protocol == r["protocol"]
               for r in allow_rules)
assert allows("10.1.2.3", 443)
assert not allows("203.0.113.5", 443)
assert not allows("10.1.2.3", 22)
print("Scoped ingress policy validated; no real networking performed.")
