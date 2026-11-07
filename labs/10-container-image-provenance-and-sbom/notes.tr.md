# Gün 10 — Konteyner İmajı Kökeni ve SBOM Temelleri

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Konteynerler uygulama ve bağımlılıkları paketler, ancak konteyner sınırı donanım izolasyonuyla aynı değildir. İmajın neyle, nerede ve hangi güven politikasıyla üretildiğini bilmek gerekir.

## Temel kavramlar ve güven sınırları

1. Digest sabitleme, etiketin beklenmedik değişikliklerini azaltır; tek başına güvenilirlik veya açıklıksızlık kanıtı değildir.

2. SBOM (Yazılım Malzeme Listesi) bileşen ve sürümleri tutarak envanter ve güvenlik açığı takibini kolaylaştırır.

3. İmza doğrulama, güvenilir build kökeni, çalışma zamanında en az yetki ve yama döngüsü farklı savunma katmanlarıdır.

## Örnek senaryo

Dağıtım digest olmadan image:latest kullanıyor ve ayrıcalıklı çalışıyor. Birbirinden bağımsız iki bulgu kaydet.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Sentetik konteyner manifestosunu ve SBOM'u incele.
2. Versiyonsuz bir bağımlılık ekle.
3. İmzalı fakat açık barındıran imajın neden yama gerektirdiğini anlat.

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
