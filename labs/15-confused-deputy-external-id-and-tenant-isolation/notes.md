# Day 15 — Cross-Account Confused Deputy, External ID and Tenant Isolation

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline practical](lab.py)

## Goal: protect access delegated to a third party
Day 14 separated **role trust** (who may assume a role) from **role permissions** (what an assumed role can do). Day 15 examines a problem that can arise when **one trusted service serves multiple customers**: the *confused deputy*.

Imagine a fictional reporting partner serving `tenant-a` and `tenant-b`. Both trust the partner to read their own quarterly report. A request purportedly made on behalf of tenant B must not accidentally cause the partner to assume a role or read a resource belonging to tenant A.

## Three independent boundaries
1. **Authenticate the requesting principal.** In real cloud systems, the service identity must be verified using the provider's actual federation or identity mechanisms. Our demo assumes the principal string is already authenticated; it **does not implement authentication**.
2. **Bind role assumption to the intended customer.** An AWS-style `ExternalId` condition can help a cross-account third-party integration avoid confused-deputy mistakes. In the toy model, each tenant has a different fictional external reference. An external ID is **not a password or authentication credential**; correct usage depends on the partner securely binding requests to the proper tenant.
3. **Constrain the resulting session.** Even after trust checks pass, an assumed role should be allowed only the necessary operations on the correct tenant's resources. Our sample permits `read` on one named report per tenant, not `delete` or cross-tenant reads.

**Trust conditions and permissions are evaluated separately.** Passing an external-ID comparison does not grant general access. Real provider policies may additionally involve session conditions, organizations, service principals, explicit deny, resource policies, session tags, identity federation and auditing.

## Run safely with no cloud account
```bash
python lab.py
```
The script uses only Python's standard library and invented identities, tenant IDs and resources. It models `AssumeRequest → Session → resource authorization`, and asserts **seven** synthetic outcomes:
- Correct A and B tenant-specific sessions may read their respective reports.
- Wrong tenant reference, untrusted principal and unknown tenant are denied.
- A valid A session cannot read B's report or delete A's report.

No AWS/Azure/GCP API requests, secrets, network traffic or modifications take place.

## Exercises
1. Explain why a cross-account trust policy that admits a third party is *not* sufficient to authorize every resource.
2. If tenant B supplies its own external reference while requesting tenant A's role, which check blocks it?
3. Why is an external ID **not** equivalent to a secret password? What additional validation must a partner perform?
4. Add a second report to tenant A while keeping tenant B isolated. What must change in the permission map?
5. Propose an audit event containing requesting principal, destination tenant, role, resource, decision and correlation ID, without exposing credentials.
6. List which assumptions of this simplified model need verification using actual AWS IAM documentation before production use.

## Scope and reference
This is an **AWS-inspired conceptual model**, not a production trust-policy parser. Cloud services differ in federation, trust conditions and organization policy semantics. Consult the provider's official guidance:
- [AWS: External ID and the confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html)
- [AWS: IAM roles and trust](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

Only perform cloud configuration tests in environments you own or are explicitly authorized to manage.
