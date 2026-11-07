# Day 02 — IAM Policies, Least Privilege and Explicit Deny

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Identity and Access Management (IAM) decides who can perform an action on a resource. A secure evaluator must consider principal, action, resource and conditions before granting access.

## Core concepts and trust boundaries

1. Least privilege gives identities only the actions needed for their tasks, for the shortest practical duration.

2. A default-deny policy rejects requests not specifically authorized; explicit denies override allows in many policy models.

3. Real cloud IAM engines include inheritance, resource policies, roles, condition keys and service-specific evaluation rules. This lab deliberately implements a smaller model.

## Guided scenario

A reporting job needs to read one dataset but should never delete it. Compare an allow rule with a separate explicit deny.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Confirm read is allowed but delete is denied.
2. Try an unlisted resource and observe default deny.
3. Describe what additional conditions a production policy engine needs.

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
