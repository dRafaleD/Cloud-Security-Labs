# Day 10 — Container Image Provenance and SBOM Basics

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Learning objective

Containers package applications and dependencies, but a container boundary is not equivalent to a hardware security boundary. Know what was built, from which materials and under which trust policy.

## Core concepts and trust boundaries

1. Immutable digest pinning helps avoid surprise tag changes; a digest alone does not prove trust or vulnerability-free software.

2. A Software Bill of Materials (SBOM) records component names and versions to support inventory and vulnerability response.

3. Signature verification, trusted build provenance, least-privilege runtime and patch lifecycle are separate layers.

## Guided scenario

A deployment uses image:latest without a digest and runs as a privileged user. Identify two independent findings.

## Offline hands-on exercise

Read `lab.py` in this folder, then run with Python 3:

```bash
python lab.py
```

The script uses only synthetic values and the Python standard library. Assertions check the intended decisions.

## Exercises

1. Examine a synthetic container manifest and SBOM.
2. Add a versionless dependency to the manifest.
3. Explain why a signed vulnerable image still needs patching.

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
