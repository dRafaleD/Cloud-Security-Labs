# Day 05 — VPCs, Subnets and Security Group Rules

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Cloud network segmentation limits which services can reach one another. A subnet route, firewall rule and application authorization check protect different boundaries.

## Core concepts and trust boundaries

1. CIDR identifies an address range, not an identity. Network location alone is insufficient authorization.

2. An ingress rule should specify protocol, ports and scoped sources; 0.0.0.0/0 often means any IPv4 source.

3. Security group semantics differ across providers (stateful/stateless, rule ordering). This lab uses a simple first-match-independent allow model.

## Guided scenario

An internal API should receive HTTPS from 10.1.0.0/16 but reject random internet clients and SSH.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Verify that 10.1.2.3:443 passes and 203.0.113.5:443 fails.
2. Try port 22 from the internal range.
3. Explain why this model does not simulate routing or return traffic.

## Review questions

1. Who controls the inputs? Which fields are untrusted?
2. Separate the program's direct observation from your interpretation.
3. Add a negative or false-positive case and explain it.
4. How does this toy model differ from a production cloud platform?

## Safety and limitations

No live account, credentials, billable service or external target is required. Results do **not prove** a real environment is secure. Validate production controls against provider documentation and authorized tests.

## Recommended references

- [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [CISA Cloud Security](https://www.cisa.gov/topics/cybersecurity-best-practices/cloud-security)
