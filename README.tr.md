# Cloud Security Labs

[🇬🇧 English](README.md) · [🇹🇷 Türkçe](README.tr.md)

Cloud Security alanını temelden öğrenmek için hazırlanmış **14 günlük iki dilli eğitim programı**. IAM, depolama, ağ, denetim logları, sır yönetimi ve olay müdahalesini ele alır.

## Dersler

| Gün | Konu | Notlar | Uygulama |
| --- | --- | --- | --- |
| 01 | Paylaşılan Sorumluluk ve Bulut Varlık Envanteri | [Türkçe](labs/01-shared-responsibility-and-asset-inventory/notes.tr.md) · [English](labs/01-shared-responsibility-and-asset-inventory/notes.md) | [lab.py](labs/01-shared-responsibility-and-asset-inventory/lab.py) |
| 02 | IAM Politikaları, En Az Yetki ve Açık Ret | [Türkçe](labs/02-iam-least-privilege-and-explicit-deny/notes.tr.md) · [English](labs/02-iam-least-privilege-and-explicit-deny/notes.md) | [lab.py](labs/02-iam-least-privilege-and-explicit-deny/lab.py) |
| 03 | Roller, Geçici Kimlik Bilgileri ve Süre Sonu | [Türkçe](labs/03-roles-temporary-credentials-and-expiry/notes.tr.md) · [English](labs/03-roles-temporary-credentials-and-expiry/notes.md) | [lab.py](labs/03-roles-temporary-credentials-and-expiry/lab.py) |
| 04 | Nesne Depolama Açıklığı ve Erişim Politikaları | [Türkçe](labs/04-object-storage-public-exposure-and-access/notes.tr.md) · [English](labs/04-object-storage-public-exposure-and-access/notes.md) | [lab.py](labs/04-object-storage-public-exposure-and-access/lab.py) |
| 05 | VPC, Alt Ağlar ve Güvenlik Grubu Kuralları | [Türkçe](labs/05-vpcs-subnets-and-security-group-rules/notes.tr.md) · [English](labs/05-vpcs-subnets-and-security-group-rules/notes.md) | [lab.py](labs/05-vpcs-subnets-and-security-group-rules/lab.py) |
| 06 | Bulut Denetim Logları ve Olay Korelasyonu | [Türkçe](labs/06-audit-logging-and-event-correlation/notes.tr.md) · [English](labs/06-audit-logging-and-event-correlation/notes.md) | [lab.py](labs/06-audit-logging-and-event-correlation/lab.py) |
| 07 | Aktarımda ve Depoda Şifreleme, Anahtar Yaşam Döngüsü | [Türkçe](labs/07-encryption-transit-rest-and-key-lifecycle/notes.tr.md) · [English](labs/07-encryption-transit-rest-and-key-lifecycle/notes.md) | [lab.py](labs/07-encryption-transit-rest-and-key-lifecycle/lab.py) |
| 08 | Sır Yönetimi ve Güvenli Loglama | [Türkçe](labs/08-secrets-management-and-safe-logging/notes.tr.md) · [English](labs/08-secrets-management-and-safe-logging/notes.md) | [lab.py](labs/08-secrets-management-and-safe-logging/lab.py) |
| 09 | Instance Metadata Güveni ve SSRF Sınırları | [Türkçe](labs/09-instance-metadata-trust-and-ssrf-boundaries/notes.tr.md) · [English](labs/09-instance-metadata-trust-and-ssrf-boundaries/notes.md) | [lab.py](labs/09-instance-metadata-trust-and-ssrf-boundaries/lab.py) |
| 10 | Konteyner İmajı Kökeni ve SBOM Temelleri | [Türkçe](labs/10-container-image-provenance-and-sbom/notes.tr.md) · [English](labs/10-container-image-provenance-and-sbom/notes.md) | [lab.py](labs/10-container-image-provenance-and-sbom/lab.py) |
| 11 | Infrastructure as Code Yapılandırma Denetimi | [Türkçe](labs/11-infrastructure-as-code-policy-checks/notes.tr.md) · [English](labs/11-infrastructure-as-code-policy-checks/notes.md) | [lab.py](labs/11-infrastructure-as-code-policy-checks/lab.py) |
| 12 | Bulut Olay Müdahalesi: Korelasyon Bitirme Çalışması | [Türkçe](labs/12-cloud-incident-response-capstone/notes.tr.md) · [English](labs/12-cloud-incident-response-capstone/notes.md) | [lab.py](labs/12-cloud-incident-response-capstone/lab.py) |
| 13 | Bulut Kaynak Etiketleri ve Sahiplik Değişimi | [Türkçe](labs/13-cloud-resource-tagging-and-owner-drift/notes.tr.md) · [English](labs/13-cloud-resource-tagging-and-owner-drift/notes.md) | [lab.py](labs/13-cloud-resource-tagging-and-owner-drift/lab.py) |
| 14 | Hesaplar Arası Rol Güveni ve İzin Kapsamı | [Türkçe](labs/14-cross-account-role-trust-and-permission-scope/notes.tr.md) · [English](labs/14-cross-account-role-trust-and-permission-scope/notes.md) | [lab.py](labs/14-cross-account-role-trust-and-permission-scope/lab.py) |

## Nasıl çalışılır?

1. Günün Türkçe notunu oku; İngilizce notla temel terimleri karşılaştır.
2. `lab.py` dosyasındaki kararları çalıştırmadan önce tahmin et.
3. `python lab.py` komutuyla dene; `assert` çıktısını kontrol et. Tüm labları kontrol etmek için repo kökünde `python test_all.py` çalıştır.
4. Negatif örnek ekle, sonuçları ve sınırlamaları kaydet.
5. Öğrendiklerini gerçek sağlayıcı belgeleriyle çapraz doğrula.

## Gereksinimler

- Python 3.10+ (standart kütüphane)
- Bulut hesabı, API anahtarı, ödeme yöntemi veya gerçek kaynak gerekmiyor.

## Dizin yapısı

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
    └── ... (toplam 14 gün, aynı düzen)
```

## Güvenlik ve etik

Bu eğitim yalnızca zararsız yerel simülasyonlar içerir. Gerçek AWS, Azure veya GCP ortamlarını taramaz ve yapılandırma değiştirmez. Eğitim verileri gerçek sağlayıcı davranışının tam modeli değildir.

## Devam yolu

Bu 14 günlük temel seri tamamlandıktan sonra sağlayıcıya özel (AWS/Azure/GCP), kontrollü sandbox ve ileri seviyede policy-as-code çalışmalarına geçilebilir.

