# Gün 02 — IAM Politikaları, En Az Yetki ve Açık Ret

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Kimlik ve Erişim Yönetimi (IAM), bir kimliğin hangi kaynak üzerinde hangi işlemi yapabileceğini belirler. Güvenli karar için özne, eylem, kaynak ve koşullar birlikte değerlendirilir.

## Temel kavramlar ve güven sınırları

1. En az yetki, bir kimliğe yalnızca işi için gerekli eylemleri ve mümkünse sınırlı süreyle tanımlar.

2. Varsayılan ret yaklaşımı açıkça izin verilmemiş isteği engeller; pek çok IAM modelinde açık ret, izin kuralına baskındır.

3. Gerçek bulut IAM motorları kalıtım, kaynak politikaları, rol ve koşul anahtarları içerir. Bu lab bilinçli olarak daha küçük bir model kurar.

## Örnek senaryo

Raporlama görevi bir veri kümesini okuyabilmeli fakat silememelidir. İzin ve açık ret kurallarını karşılaştır.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Okuma izninin çalıştığını, silmenin reddedildiğini doğrula.
2. Listede olmayan kaynak için varsayılan reti gözlemle.
3. Üretim IAM kararında hangi ek koşulların gerektiğini tartış.

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
