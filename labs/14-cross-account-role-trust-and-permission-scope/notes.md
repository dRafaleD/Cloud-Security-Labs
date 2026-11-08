# Day 14 — Cross-Account Role Trust and Permission Scope

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline practical](lab.py)

## Why cross-account access needs two checks
Large cloud environments separate workloads, teams and billing into accounts, projects or subscriptions. A role may be assumed by a different security principal, but granting **trust to assume a role** is not the same as giving that role unrestricted permission over every resource.

## Two distinct policy questions
1. **Who may assume the role?** A trust/federation policy identifies trusted external identities. For real services, account identity, issuer, audience, conditional claims and external IDs may matter.
2. **What can the assumed role do?** A permission policy restricts operations and resources. A trusted identity should still receive only the minimum permissions required.

A permissive trust rule can admit unwanted principals. A narrow permission set reduces impact but does not fix the trust mistake. Conversely, correct trust does not compensate for an overpowered role. Production engines also enforce denies, boundaries, organization policies, sessions and resource policies.

## Local exercise
```bash
python lab.py
```
The simulation uses invented identifiers, such as `tenant-a:reporter` and `report:quarterly`. It grants the reporting role read access to exactly one report. It denies an untrusted identity, a delete operation and a different resource. **No cloud APIs or credentials are used.**

## Exercises
1. Predict the five validation outcomes.
2. Add `tenant-b:analyst` to the trusted-principal set. Does that automatically grant export?
3. Explain how a stolen credential and an overly broad trust policy create different risks.
4. Propose auditable logs for failed role assumption, granted sessions and resource actions.
5. List vendor-specific controls you would need before adapting the model to AWS/Azure/GCP.

## Evidence and limits
The script demonstrates **policy composition**, not a real IAM policy evaluator or proof of production safety. Testing requires the provider's current IAM semantics and an expressly authorized environment.

## References
- [AWS IAM roles and trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Microsoft Entra workload identities](https://learn.microsoft.com/en-us/entra/workload-id/)
- [Google Cloud IAM](https://cloud.google.com/iam/docs/overview)
