# Day 08 — Secrets Management and Safe Logging

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

API keys, passwords and connection strings should not live in source repositories or plaintext logs. Workloads should receive only secrets they need, from a controlled channel.

## Core concepts and trust boundaries

1. Use a dedicated secrets manager or platform identity mechanism; environment variables may still be exposed via dumps or misconfiguration.

2. Redaction removes or masks sensitive values before logs, errors and telemetry are stored. It must be tested with negative and boundary examples.

3. Secret scanning catches some patterns but has false negatives. Rotation and access review still matter after any possible exposure.

## Guided scenario

A test application accidentally logs DEMO_TOKEN=example-value. Ensure its structured logger masks the value without hiding useful event context.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Run the redaction test and add a second synthetic field.
2. Discuss why post-hoc deletion is weaker than preventing storage.
3. List logs and CI artifacts that may retain leaked secrets.

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
