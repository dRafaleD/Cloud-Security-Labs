# Gün 13 — Bulut Kaynak Etiketleri ve Sahiplik Değişimi

[English](notes.md) · [Türkçe](notes.tr.md) · [Uygulama](lab.py)

## Öğrenme amacı

Zararsız yerel veriyle **Bulut Kaynak Etiketleri ve Sahiplik Değişimi** konusunun güven sınırlarını ve kanıt değerlendirmesini öğren.

## Temel kavramlar

1. Bulut etiketleri envanter, maliyet ve olay müdahalesini kolaylaştırır; ancak kullanıcıların değiştirebildiği metadata olup değişmez kimlik kanıtı değildir.

2. Bilinen envanterle mevcut özellikleri karşılaştırarak sahipsiz varlıkları ve ortam değişimlerini belirle.

3. Etiket kuralları tek başına erişimi engellemez; gerçek IAM ve sağlayıcı politikaları gerekir.

## Güvenli pratik

Önce kaynak kodunu oku ve sonucu tahmin et:

```bash
python lab.py
```

Çıktı sentetiktir; gerçek sisteme komut gönderilmez.

## Görevler

1. Girdi verisini ve güvenilmeyen alanları belirle.
2. Bir negatif ya da sınır örneği ekleyip test et.
3. Gözlem ve yorum farkını açıkla.
4. Gerçek ortamda hangi doğrulamaların gerektiğini yaz.

## Kontrol soruları

- Tek gösterge yeterli mi?
- Yanlış pozitif veya eksik kayıt nasıl oluşabilir?
- Sonucu tekrar üretmek için hangi girdileri saklamalısın?

## Güvenlik ve sınırlamalar

Bu çalışma gerçek malware, bulut hesabı, sistem müdahalesi veya dış ağ gerektirmez. Modelin basitliği gerçek platformla birebir eşitlik iddiası taşımaz.
