# Day 09 — Instance Metadata Trust and SSRF Boundaries

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Some cloud environments expose instance metadata to workloads through a local endpoint. A server-side request forgery bug may turn remote input into unauthorized internal requests.

## Core concepts and trust boundaries

1. IMDSv2-style token checks reduce some metadata access risks, but are not a substitute for application-side URL allowlists and egress control.

2. URL validation must account for redirects, DNS resolution, IP classifications and rebinding risk. A string-prefix check is insufficient.

3. Treat metadata responses as sensitive. This lab never accesses real metadata endpoints or retrieves credentials.

## Guided scenario

A web app fetches a URL specified by a user. Describe how to enforce a trusted destination policy before making any request.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Run the offline token-required model.
2. Try the missing-token and expired-token cases.
3. Explain why a real SSRF defense must validate actual resolution and redirects.

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
