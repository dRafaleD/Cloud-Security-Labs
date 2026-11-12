# Gün 16 — Geçici Oturumlar, Süre Sonu ve Yetki Kapsamı

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 15. günden devam
Önceki gün, farklı hesapların rol güven ilişkisini ve `external ID` kontrolünü işledik. Şimdi bir rol oturumu oluşturulduktan sonra **hangi işlemlere, ne kadar süreyle izin verildiğini** inceliyoruz.

**Temporary credentials (geçici kimlik bilgileri):** belirli süre sonunda geçersiz olan oturum kimliği.
**Session scope:** işlem yetkisinin kullanıcı, tenant, eylem ve kaynağa göre sınırlandırılması.
**TTL:** oturumun geçerli kalabileceği süre.
**Expiry:** sürenin dolması.

## Basit eğitim modeli
İki hayalî tenant ve bir partner var. Tenant'a ait doğru referans verilirse yalnızca o tenant'ın raporu için **okuma** yetkili oturum oluşturuluyor. İsteğin sahibi, kaynak, işlem ve zaman her çağrıda yeniden kontrol ediliyor.

Bu modelde geçerli zaman:
`issued_at <= now < expires_at`

Yani süre bitiş saniyesine gelindiği anda erişim reddedilir. Başka tenant, başka kaynak, yazma işlemi, yanlış principal veya hatalı external ID reddedilir.

## Çalıştırma
~~~bash
python3 labs/16-temporary-sessions-expiry-and-scoped-actions/lab.py
python3 test_all.py
~~~
Gerçek bulut hesabı veya API anahtarı gerekmez. Zaman damgaları bile uydurmadır.

## Sorular
1. Doğru rolü almak neden sınırsız yetki vermez?
2. Geçici oturumlar neden süreye ihtiyaç duyar?
3. Tam sürenin dolduğu anda ne olmalı?
4. Kaynak yetkisi her istekte neden tekrar denetlenir?
5. Gerçek bulut servisinde sızan bir oturuma karşı ek olarak ne gerekir?

## Sınırlar
Bu model gerçek bulut sağlayıcılarının yetkilendirme davranışını taklit etme iddiası taşımaz. Tamamen yerel ve sentetiktir.
