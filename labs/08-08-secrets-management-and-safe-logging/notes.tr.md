# Gün 08 — Sır Yönetimi ve Güvenli Loglama

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

API anahtarı, parola ve bağlantı dizgeleri kaynak kod depolarında veya düz metin loglarında tutulmamalıdır. İş yüküne yalnız ihtiyacı olan sırlar güvenilir bir kanal üzerinden verilmelidir.

## Temel kavramlar ve güven sınırları

1. Secrets manager veya platform kimliği kullan; ortam değişkenleri bile dump ve hatalı yapılandırmayla açığa çıkabilir.

2. Maskeleme (redaction), loglama öncesi gizli değerleri kaldırır. Pozitif, negatif ve sınır örnekleriyle test edilmelidir.

3. Secret scanner bazı biçimleri bulur, ancak her sırrı yakalamaz. Sızıntı şüphesinde rotasyon ve yetki gözden geçirme önemlidir.

## Örnek senaryo

Test uygulaması yanlışlıkla DEMO_TOKEN=example-value logluyor. Yapılandırılmış loglayıcının değeri maskeleyip olay bağlamını koruduğunu göster.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Maskeleme testini çalıştır ve ikinci bir sentetik alan ekle.
2. Kaydettikten sonra silmenin, en başta kaydetmemekten neden zayıf olduğunu anlat.
3. Sırların kalabileceği log ve CI çıktıları için kontrol listesi oluştur.

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
