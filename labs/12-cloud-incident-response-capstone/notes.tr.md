# Gün 12 — Bulut Olay Müdahalesi: Korelasyon Bitirme Çalışması

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Bulut olay müdahalesi kimlik, kaynak, ağ ve denetim günlüklerini birleştirir. Güvenilir analiz, kaydın doğrudan gösterdiği şey ile şüpheyi ayırır.

## Temel kavramlar ve güven sınırları

1. UTC zaman çizelgesi oluştur; kaynak olay kimliklerini koru ve eksik delilleri belirt.

2. Oturum iptali, yetki kısıtlama ve açık erişimi kapatma gibi önlemler iş kesintisi doğurabilir ve yetki gerektirir.

3. Hipotezle ilerle: sıra dışı işlem tek başına kötü niyet kanıtı değildir. Bağımsız telemetriyle doğrula.

## Örnek senaryo

Sentetik bir oturum yeni kaynaktan giriş sonrası depolama politikası değiştiriyor. Doğrudan gözlem ve yanıtlanmamış soruları içeren yapılandırılmış bulgu üret.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Zaman çizelgesini çalıştır ve delil nesnelerini kontrol et.
2. Gözlem, çıkarım ve güven düzeyini ayıran rapor yaz.
3. Yetkili müdahale ve geri alma kontrol listesi hazırla.

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
