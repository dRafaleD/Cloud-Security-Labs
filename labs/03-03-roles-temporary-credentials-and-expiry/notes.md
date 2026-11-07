# Day 03 — Roles, Temporary Credentials and Expiry

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Applications should favor short-lived identity mechanisms over long-lived secrets where the platform supports them. A role is a set of permissions; a temporary session is a time-limited grant.

## Core concepts and trust boundaries

1. Credential lifetime limits exposure after accidental disclosure, but revocation, rotation and logging are still important.

2. Identity federation uses a trusted issuer to provide scoped access without distributing permanent keys to every workload.

3. Expiry checks need trustworthy server-side time. Local clock skew can cause mistaken accept/reject decisions.

## Guided scenario

A synthetic service obtains a read-only session for ten minutes. Check access just before and exactly at expiry.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Trace issued_at and expires_at boundaries.
2. Add a request for a forbidden action.
3. Explain what session revocation would require.

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
