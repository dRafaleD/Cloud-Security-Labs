# Gün 11 — Infrastructure as Code Yapılandırma Denetimi

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Infrastructure as Code (IaC) altyapıyı tekrar üretilebilir yapar; fakat hatalı yapılandırmayı da tekrar edebilir. Politika kontrolleri gerçek değişiklik uygulanmadan önce çalıştırılmalıdır.

## Temel kavramlar ve güven sınırları

1. Yapılandırmayı incelenebilir kod olarak gör; hassas değişikliklerde kod incelemesi, plan/diff ve politika doğrulaması uygula.

2. Tarayıcı potansiyel risk işaretler; kanıtı saklamalı ve gerekçeli istisnaları ele almalıdır.

3. Gerçek kontroller sağlayıcıya özel şema, kimlik bağlamı, modül çözümleme ve kaynak ilişkilerini bilmeyi gerektirir.

## Örnek senaryo

Yeni kaynak yapılandırması SSH portunu internete açıp denetim loglarını kapatıyor. Dağıtımdan önce iki sorunu da yakala.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Çevrimdışı yapılandırma denetimini çalıştır.
2. Güvenli varsayılanlara sahip örnek ekleyip karşılaştır.
3. Bu basit sözlük kontrolünün neden gerçek Terraform doğrulaması olmadığını anlat.

## Değerlendirme soruları

1. Girdi ve verinin sahibi kim? Hangi alanlar güvenilir sayılmamalı?
2. Programın doğrudan gözlemi ile senin yorumunu ayır.
3. Olumsuz durum / yanlış pozitif örneği ekle ve nedenini açıkla.
4. Bu sentetik modelin gerçek bulut sağlayıcısından farkı nedir?

## Güvenlik, etik ve sınırlamalar

Canlı hesap, gerçek kimlik bilgisi, ücretli servis veya dış hedef gerekmez. Bu sonuçlar gerçek ortamın güvenli olduğunu **kanıtlamaz**. Üretim ortamındaki kurallar sağlayıcı belgeleri ve yetkili testlerle doğrulanmalıdır.

## Önerilen kaynaklar

- [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [CISA Cloud Security](https://www.cisa.gov/topics/cybersecurity-best-practices/cloud-security)
