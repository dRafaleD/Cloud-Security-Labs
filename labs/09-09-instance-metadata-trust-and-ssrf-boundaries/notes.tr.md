# Gün 09 — Instance Metadata Güveni ve SSRF Sınırları

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Bazı bulut ortamlarda örnek (instance) metadatası yerel bir uç noktada bulunur. SSRF açığı, dışarıdan kontrol edilen URL'yi sunucunun istenmeyen iç isteğe dönüştürmesine neden olabilir.

## Temel kavramlar ve güven sınırları

1. IMDSv2 benzeri oturum token kontrolleri bazı erişimleri kısıtlar; ancak uygulama tarafında URL izin listesi ve çıkış kısıtları da gereklidir.

2. URL doğrulaması yönlendirme, DNS çözümleme, IP sınıflandırması ve yeniden bağlama (rebinding) riskini dikkate almalı; basit metin başlangıcı kontrolü yetmez.

3. Metadata yanıtı hassas olabilir. Bu lab gerçek metadata uç noktasına erişmez ve kimlik bilgisi almaz.

## Örnek senaryo

Web uygulaması kullanıcının belirttiği URL'yi çekiyor. İstek yapılmadan önce güvenilen hedef politikasını nasıl uygulayacağını açıkla.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Token gerektiren çevrimdışı modeli çalıştır.
2. Eksik ve süresi dolmuş token durumunu incele.
3. Gerçek SSRF savunmasının yönlendirme ve çözümlemeyi neden denetlediğini açıkla.

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
