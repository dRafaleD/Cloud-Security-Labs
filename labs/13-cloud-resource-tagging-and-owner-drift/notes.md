# Day 13 — Cloud Resource Tagging and Ownership Drift

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Learning objective

Learn the trust and evidence boundaries of **Cloud Resource Tagging and Ownership Drift** using harmless local fixtures.

## Core concepts

1. Cloud resource tags help inventory, cost attribution and incident response, but tags are user-controlled metadata rather than immutable identity proof.

2. Compare a known-good inventory against observed resource attributes to detect missing owners and environment transitions.

3. Tagging rules alone cannot block resource access; enforce permissions with actual IAM and provider policies.

## Safe hands-on

Read the code and predict its output before running:

```bash
python lab.py
```

Output is synthetic; no operations are sent to a live target.

## Assignments

1. Identify input provenance and untrusted fields.
2. Add and test a negative or boundary case.
3. Separate direct observations from interpretations.
4. Describe additional validation needed in a real environment.

## Knowledge check

- Is any single indicator sufficient?
- What can cause false positives or missing evidence?
- What inputs are needed to reproduce the result?

## Safety and limitations

No live malware, cloud accounts, system modifications, or outbound traffic. This minimal model is not an exact platform implementation.
