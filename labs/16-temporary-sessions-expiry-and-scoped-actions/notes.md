# Day 16 — Temporary Sessions, Expiry and Scoped Cloud Actions

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline exercise](lab.py)

## Connection to Day 15
Day 15 modeled cross-account role trust, external IDs and tenant isolation. Day 16 explores what happens **after** an authorized session is issued: it must be short-lived and limited to the intended resources and actions.

**Temporary credentials:** credentials with a bounded lifetime, unlike permanent account keys. **Session scope:** what principal, tenant, action and resource may be used. **Expiry:** a time at which the session must stop granting access.

## Harmless Python model
The fixture uses two fictional tenants and a known partner principal. A session is issued only if tenant-specific trust and an external-ID string match. The session grants **read** access to exactly one tenant's report, with an issue time and maximum TTL. Time is a synthetic integer, not an external clock.

The local checks cover start time, just before expiry, exactly at expiry, before issue, write denial, cross-tenant denial, resource mismatch, principal mismatch, invalid external ID and invalid TTL.

A session is valid during the half-open interval `issued_at <= now < expires_at`. This makes the expiry boundary unambiguous. Real cloud providers have additional policies, trust conditions and credential formats; the model does not reproduce AWS STS, Azure or GCP behavior.

## Run
~~~bash
python3 labs/16-temporary-sessions-expiry-and-scoped-actions/lab.py
python3 test_all.py
~~~
Both run offline. The repository-wide runner is updated to include 16 labs.

## Questions
1. Why does assuming a role not imply every action is allowed?
2. Why is authorization checked again for each requested resource?
3. What should happen at the exact expiration timestamp?
4. What are the trade-offs of very long or short session TTLs?
5. What additional measures would real cloud credentials need against theft or replay?

## Scope
Only a synthetic policy model; no cloud accounts, APIs, secrets or real session tokens.
