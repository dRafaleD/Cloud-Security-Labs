# Day 07 — Encryption in Transit, at Rest and Key Lifecycle

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Encryption protects different threat boundaries depending on where it is applied. Evaluate transport security, storage protection and key-management permissions separately.

## Core concepts and trust boundaries

1. TLS helps protect data in transit when endpoint identity is verified; merely seeing an HTTPS scheme is not sufficient to judge the configuration.

2. At-rest encryption protects stored bytes under defined conditions, but does not replace access control or backup protections.

3. Key rotation, revocation, audit access, separation of duties and disaster recovery are part of cryptographic operations. Avoid implementing your own cryptography.

## Guided scenario

A backup is encrypted but an over-privileged service account can still export it. Identify the missing control.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Evaluate synthetic records for missing TLS, rest encryption or restricted key access.
2. Explain why all three controls are distinct.
3. Document one real-world key-rotation risk.

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
