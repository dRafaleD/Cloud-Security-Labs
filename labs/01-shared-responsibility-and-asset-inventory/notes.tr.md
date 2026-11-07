# Gün 01 — Paylaşılan Sorumluluk ve Bulut Varlık Envanteri

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Bulut güvenliğinde ilk adım, hangi güvenlik kontrollerinin sağlayıcıya, hangilerinin müşteriye ait olduğunu anlamaktır. IaaS, PaaS ve SaaS sorumluluk dağılımını değiştirir; müşterinin sorumluluğunu sıfırlamaz.

## Temel kavramlar ve güven sınırları

1. Fiziksel veri merkezi güvenliği çoğunlukla sağlayıcıya aittir; kimlik izinleri, veri sınıflandırması ve tenant yapılandırması müşterinin sorumluluğundadır.

2. IaaS'ta konuk işletim sistemi yamaları çoğu zaman müşteriye aittir; PaaS genelde alttaki işletim sistemini soyutlar. Somut hizmet şartları kontrol edilmelidir.

3. Envanter; sahip, ortam, bölge, hassasiyet ve yaşam döngüsü bilgisi içermelidir. Sahibi bilinmeyen varlık olay müdahalesini zorlaştırır.

## Örnek senaryo

Bir ekip veritabanını yönetilen hizmete taşıyıp tüm veri erişim politikalarının artık sağlayıcıya ait olduğunu sanıyor. Eksik kalan kontrolleri belirle.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Simülatörü çalıştırıp IaaS/PaaS/SaaS sonuçlarını karşılaştır.
2. Sahibi tanımlı sentetik nesne depolama varlığı ekle.
3. Bu çıktının neden gerçek hizmet sözleşmesi değil örnek model olduğunu açıkla.

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
