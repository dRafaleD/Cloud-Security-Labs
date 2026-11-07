# Day 06 — Cloud Audit Logs and Event Correlation

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

An audit record should help answer who did what, to which resource, from where and when. Disabling logs or collecting incomplete fields limits incident investigations.

## Core concepts and trust boundaries

1. Use normalized UTC timestamps and stable event IDs. Keep the original event when constructing an analyst timeline.

2. Authentication events, permission changes and resource access may live in different audit streams; correlate rather than assuming one is complete.

3. A single alert is a lead, not proof. Measure the potential for benign administrative changes and duplicated events.

## Guided scenario

A synthetic account sees failed sign-ins followed by a policy change. Produce a timeline without claiming compromise from the sequence alone.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Sort records by UTC timestamp and event ID.
2. Identify the principal and resource associated with a sensitive change.
3. Discuss what independent evidence you would request.

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
