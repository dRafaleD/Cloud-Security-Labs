# Cloud Security Labs

[🇬🇧 English](README.md) · [🇹🇷 Türkçe](README.tr.md)

A **15-day bilingual learning path** from cloud fundamentals to IAM, storage, network boundaries, audit logging, secret handling and incident response.

## Labs

| Day | Topic | Notes | Practice |
| --- | --- | --- | --- |
| 01 | Shared Responsibility and Cloud Asset Inventory | [English](labs/01-shared-responsibility-and-asset-inventory/notes.md) · [Türkçe](labs/01-shared-responsibility-and-asset-inventory/notes.tr.md) | [lab.py](labs/01-shared-responsibility-and-asset-inventory/lab.py) |
| 02 | IAM Policies, Least Privilege and Explicit Deny | [English](labs/02-iam-least-privilege-and-explicit-deny/notes.md) · [Türkçe](labs/02-iam-least-privilege-and-explicit-deny/notes.tr.md) | [lab.py](labs/02-iam-least-privilege-and-explicit-deny/lab.py) |
| 03 | Roles, Temporary Credentials and Expiry | [English](labs/03-roles-temporary-credentials-and-expiry/notes.md) · [Türkçe](labs/03-roles-temporary-credentials-and-expiry/notes.tr.md) | [lab.py](labs/03-roles-temporary-credentials-and-expiry/lab.py) |
| 04 | Object Storage Exposure and Access Policies | [English](labs/04-object-storage-public-exposure-and-access/notes.md) · [Türkçe](labs/04-object-storage-public-exposure-and-access/notes.tr.md) | [lab.py](labs/04-object-storage-public-exposure-and-access/lab.py) |
| 05 | VPCs, Subnets and Security Group Rules | [English](labs/05-vpcs-subnets-and-security-group-rules/notes.md) · [Türkçe](labs/05-vpcs-subnets-and-security-group-rules/notes.tr.md) | [lab.py](labs/05-vpcs-subnets-and-security-group-rules/lab.py) |
| 06 | Cloud Audit Logs and Event Correlation | [English](labs/06-audit-logging-and-event-correlation/notes.md) · [Türkçe](labs/06-audit-logging-and-event-correlation/notes.tr.md) | [lab.py](labs/06-audit-logging-and-event-correlation/lab.py) |
| 07 | Encryption in Transit, at Rest and Key Lifecycle | [English](labs/07-encryption-transit-rest-and-key-lifecycle/notes.md) · [Türkçe](labs/07-encryption-transit-rest-and-key-lifecycle/notes.tr.md) | [lab.py](labs/07-encryption-transit-rest-and-key-lifecycle/lab.py) |
| 08 | Secrets Management and Safe Logging | [English](labs/08-secrets-management-and-safe-logging/notes.md) · [Türkçe](labs/08-secrets-management-and-safe-logging/notes.tr.md) | [lab.py](labs/08-secrets-management-and-safe-logging/lab.py) |
| 09 | Instance Metadata Trust and SSRF Boundaries | [English](labs/09-instance-metadata-trust-and-ssrf-boundaries/notes.md) · [Türkçe](labs/09-instance-metadata-trust-and-ssrf-boundaries/notes.tr.md) | [lab.py](labs/09-instance-metadata-trust-and-ssrf-boundaries/lab.py) |
| 10 | Container Image Provenance and SBOM Basics | [English](labs/10-container-image-provenance-and-sbom/notes.md) · [Türkçe](labs/10-container-image-provenance-and-sbom/notes.tr.md) | [lab.py](labs/10-container-image-provenance-and-sbom/lab.py) |
| 11 | Infrastructure as Code Policy Checks | [English](labs/11-infrastructure-as-code-policy-checks/notes.md) · [Türkçe](labs/11-infrastructure-as-code-policy-checks/notes.tr.md) | [lab.py](labs/11-infrastructure-as-code-policy-checks/lab.py) |
| 12 | Cloud Incident Response: Correlation Capstone | [English](labs/12-cloud-incident-response-capstone/notes.md) · [Türkçe](labs/12-cloud-incident-response-capstone/notes.tr.md) | [lab.py](labs/12-cloud-incident-response-capstone/lab.py) |
| 13 | Cloud Resource Tagging and Ownership Drift | [English](labs/13-cloud-resource-tagging-and-owner-drift/notes.md) · [Türkçe](labs/13-cloud-resource-tagging-and-owner-drift/notes.tr.md) | [lab.py](labs/13-cloud-resource-tagging-and-owner-drift/lab.py) |
| 14 | Cross-Account Role Trust and Permission Scope | [English](labs/14-cross-account-role-trust-and-permission-scope/notes.md) · [Türkçe](labs/14-cross-account-role-trust-and-permission-scope/notes.tr.md) | [lab.py](labs/14-cross-account-role-trust-and-permission-scope/lab.py) |
| 15 | Confused Deputy, External ID and Tenant Isolation | [English](labs/15-confused-deputy-external-id-and-tenant-isolation/notes.md) · [Türkçe](labs/15-confused-deputy-external-id-and-tenant-isolation/notes.tr.md) | [lab.py](labs/15-confused-deputy-external-id-and-tenant-isolation/lab.py) |

## How to study

1. Read one day's notes, then compare the terminology in the other language.
2. Predict the script's behavior before execution.
3. Run `python lab.py` and inspect assertions. To check all 15 labs from the repository root, run `python test_all.py`.
4. Add a negative case and document limitations.
5. Compare assumptions with official provider documentation.

## Requirements

- Python 3.10+ (standard library)
- No cloud account, API key, payment method or real infrastructure required.

## Repository structure

```text
Cloud-Security-Labs/
├── README.md
├── README.tr.md
├── resources.md
└── labs/
    ├── 01-shared-responsibility-and-asset-inventory/
    │   ├── notes.md
    │   ├── notes.tr.md
    │   └── lab.py
    └── ... (15 days total, same layout)
```

## Safety

All examples are safe local simulations. They do not scan or change real AWS, Azure or GCP resources. Toy policy engines are not exact representations of provider behavior.

## Next steps

After these 15 foundational labs, continue with provider-specific AWS/Azure/GCP sandbox exercises, policy-as-code and advanced incident response.


## Latest lab

- **Day 15 — Confused Deputy, External ID and Tenant Isolation**
- [English notes](labs/15-confused-deputy-external-id-and-tenant-isolation/notes.md) · [Türkçe notlar](labs/15-confused-deputy-external-id-and-tenant-isolation/notes.tr.md) · [Offline Python practice](labs/15-confused-deputy-external-id-and-tenant-isolation/lab.py)
