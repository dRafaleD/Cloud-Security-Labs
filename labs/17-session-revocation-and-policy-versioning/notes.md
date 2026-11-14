# Day 17 — Session Revocation and Policy Versioning

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python practice](lab.py)

## Day 16 follow-up
A short-lived cloud session may be valid by expiry time but should sometimes lose access **earlier**: an operator revokes the session, or an organization changes its permissions.

This fictional exercise checks tenant, action, resource, issue/expiry times, a session revocation set and a **policy version**. Changing tenant policy from version 1 to version 2 invalidates older toy sessions. Explicitly revoking a newer session denies it immediately. Failure to find a session denies by default.

## Run
```bash
python3 labs/17-session-revocation-and-policy-versioning/lab.py
python3 test_all.py
```

## Questions
How does expiry differ from revocation? What if a service has stale policy caches? How quickly can a provider propagate changes? Why is this local model not proof of the behavior of AWS STS, Azure or GCP tokens?

## Limits
No real credentials or cloud APIs. Production systems have provider-specific credential caching, revocation and consistency guarantees.
