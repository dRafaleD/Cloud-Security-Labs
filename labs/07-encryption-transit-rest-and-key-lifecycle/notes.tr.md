# Gün 07 — Aktarımda ve Depoda Şifreleme, Anahtar Yaşam Döngüsü

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Şifreleme hangi katmanda uygulandığına göre farklı riskleri azaltır. Ağ trafiği, depolama ve anahtar yönetimi izinlerini birbirinden ayrı değerlendirmek gerekir.

## Temel kavramlar ve güven sınırları

1. TLS, uç nokta kimliği doğru doğrulandığında aktarımdaki veriyi korumaya yardım eder; URL'de HTTPS görmek tek başına yeterli denetim değildir.

2. Depoda şifreleme belirli koşullarda saklanan baytları korur ancak erişim yetkisi ve yedek güvenliği yerine geçmez.

3. Anahtar rotasyonu, iptal, erişim logları, görev ayrılığı ve kurtarma planı kriptografik operasyonun parçalarıdır. Kendi şifreleme algoritmanı yazma.

## Örnek senaryo

Yedek şifreli ancak gereğinden fazla yetkili servis hesabı dışa aktarabiliyor. Eksik kontrolü belirle.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. TLS, depoda şifreleme ve anahtar erişimi eksiklerini sentetik kayıtlarda bul.
2. Üç kontrolün neden farklı olduğunu açıkla.
3. Gerçek anahtar rotasyonundaki bir riski not et.

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
