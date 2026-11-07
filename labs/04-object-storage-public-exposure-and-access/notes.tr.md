# Gün 04 — Nesne Depolama Açıklığı ve Erişim Politikaları

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Nesne depolamada yedekler, günlükler ve uygulama dosyaları tutulabilir. Bağlantı oluşturulabiliyor olması nesnenin herkese açık olması gerektiği anlamına gelmez; erişim politikası veri hassasiyetiyle uyumlu olmalıdır.

## Temel kavramlar ve güven sınırları

1. Hesap düzeyi public access block, bucket politikası ve nesne izinleri birlikte incelenir; sağlayıcıların uygulama ayrıntıları değişir.

2. Uygunsa kimliğe bağlı, kısa ömürlü erişim tercih et; hassas kayıtları kalıcı olarak listeleme.

3. Depolama şifrelemesi, gereğinden fazla yetkili bir kimliğin veriyi indirmesini engellemez.

## Örnek senaryo

Bir ekip yanlışlıkla iç yedeği public işaretliyor. Hesap düzeyindeki engelin anonim isteği reddettiğini doğrula.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Anonim katalog erişimi ile iç yedek erişimini karşılaştır.
2. block_public_access değerini değiştirerek etkisini gözlemle.
3. Gerçek depolama hizmetinde hangi alanların denetlenmesi gerektiğini yaz.

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
