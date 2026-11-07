# Day 04 — Object Storage Exposure and Access Policies

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Object storage often holds backups, logs and artifacts. A public URL does not automatically mean an object should be publicly readable; access policy and data sensitivity must align.

## Core concepts and trust boundaries

1. Evaluate account-level public-access blocks, bucket-level policy and object grants together; provider semantics differ.

2. Prefer identity-scoped and short-lived access where appropriate; avoid permanent public listing of sensitive records.

3. Encryption at rest does not stop an authenticated but over-privileged identity from downloading data.

## Guided scenario

A team marks an internal backup as public by mistake. Model an account-wide override and verify anonymous requests are blocked.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Compare anonymous access to the public catalog and internal backup.
2. Switch block_public_access and observe the changed decision.
3. Identify which attributes need auditing in real storage services.

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
