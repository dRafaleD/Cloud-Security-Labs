# Gün 06 — Bulut Denetim Logları ve Olay Korelasyonu

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Denetim kaydı, kimin ne zaman hangi kaynakta hangi işlemi yaptığını ve isteğin nereden geldiğini araştırmayı sağlar. Eksik alanlar veya kapalı loglama olay müdahalesini zayıflatır.

## Temel kavramlar ve güven sınırları

1. UTC zaman damgaları ve kararlı olay kimlikleri kullan; analiz zaman çizelgesi oluştururken kaynak kayıtlarını koru.

2. Giriş olayları, yetki değişiklikleri ve kaynak erişimleri farklı log akışlarında olabilir; hepsini ilişkilendir.

3. Tek uyarı, kesin delil değildir. Meşru yönetici değişiklikleri ve tekrarlanan kayıtlar yanlış pozitif üretebilir.

## Örnek senaryo

Sentetik hesapta başarısız girişlerden sonra politika değişikliği görülüyor. Yalnızca sıralamaya bakıp ihlal iddiasında bulunmadan zaman çizelgesi üret.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. Kayıtları UTC ve olay kimliğine göre sırala.
2. Hassas değişikliğin kimliğini ve kaynağını belirt.
3. Hangi bağımsız kanıtları talep edeceğini tartış.

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
