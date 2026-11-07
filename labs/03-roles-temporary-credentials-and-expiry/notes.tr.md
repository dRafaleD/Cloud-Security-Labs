# Gün 03 — Roller, Geçici Kimlik Bilgileri ve Süre Sonu

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Platform destekliyorsa uygulamalar uzun ömürlü sırlar yerine kısa ömürlü kimlik doğrulama mekanizmalarını tercih etmelidir. Rol izinleri tanımlar; geçici oturum bu izinleri belirli zaman aralığında taşır.

## Temel kavramlar ve güven sınırları

1. Kimlik bilgisinin kısa ömürlü olması sızıntı etkisini sınırlar; ancak iptal, rotasyon ve loglama hâlâ gerekir.

2. Kimlik federasyonu, her iş yüküne kalıcı anahtar dağıtmadan güvenilir kimlik sağlayıcı üzerinden kısıtlı erişim verebilir.

3. Geçerlilik süresi denetimi güvenilir sunucu saatine dayanmalıdır. Saat kayması yanlış karar üretebilir.

## Örnek senaryo

Sentetik bir servis on dakikalık salt-okunur oturum alıyor. Süre dolmadan hemen önce ve tam bitiş anındaki erişimi karşılaştır.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Başlangıç ve bitiş sınırlarını izle.
2. İzinsiz bir eylem denemesi ekle.
3. Oturum iptali için gereken ek sistemi açıkla.

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
