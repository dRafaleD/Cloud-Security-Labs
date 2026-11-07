# Day 01 — Shared Responsibility and Cloud Asset Inventory

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Cloud security begins with knowing which controls a provider operates and which controls the customer must configure. IaaS, PaaS and SaaS shift responsibility; they do not eliminate it.

## Core concepts and trust boundaries

1. Physical data-center security is typically handled by the provider. Identity permissions, data classification and tenant configuration remain customer concerns.

2. In IaaS, guest OS patching is often customer-managed; managed PaaS usually abstracts the underlying OS. Always verify the exact service agreement.

3. An inventory needs owner, environment, region, sensitivity and lifecycle. Unknown owners make incidents slower and cleanup riskier.

## Guided scenario

A team migrates a database to a managed service and assumes all data-access policies are now the provider's duty. Identify the missing controls.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Run the simulator and compare the IaaS/PaaS/SaaS results.
2. Add a synthetic object-storage asset with a named owner.
3. Explain why the result is an illustrative model, not a contract.

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
