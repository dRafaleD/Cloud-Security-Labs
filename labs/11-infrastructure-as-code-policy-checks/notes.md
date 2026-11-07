# Day 11 — Infrastructure as Code Policy Checks

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Infrastructure as Code (IaC) makes infrastructure reproducible, but also makes misconfigurations reproducible. Policy checks should run before a change is applied.

## Core concepts and trust boundaries

1. Treat configuration as reviewable code. Require peer review, a plan/diff and policy validation for sensitive changes.

2. A security scanner flags possible risks; it must preserve evidence and allow justified exceptions rather than blindly blocking everything.

3. Production checks need provider-specific schemas, identity context, module resolution and resource relationships.

## Guided scenario

A proposed resource configuration makes SSH available to the internet and disables audit logs. Catch both before deployment.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Run the offline configuration linter.
2. Add an example with secure defaults and compare outputs.
3. Explain why this simple dictionary check is not Terraform validation.

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
