# Day 12 — Cloud Incident Response: Correlation Capstone

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Incident response combines identity, resources, network context and audit events. A reliable analyst distinguishes what logs show from what is merely suspected.

## Core concepts and trust boundaries

1. Create a timeline in UTC, preserve source event IDs and document missing evidence.

2. Containment options include revoking sessions, reducing privileges and disabling exposed access; each has operational consequences and must be authorized.

3. Use hypothesis-driven investigation: an unusual action alone does not establish malicious intent. Confirm through independent telemetry.

## Guided scenario

A synthetic session changes a storage policy after a login from a new source. Produce a structured finding with direct observations and unanswered questions.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Run the timeline and review the evidence objects.
2. Write a report separating observation, inference and confidence.
3. Design an authorized containment plan and rollback checklist.

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
