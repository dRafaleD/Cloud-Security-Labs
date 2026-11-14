# Gün 17 — Bulut Oturumlarını İptal Etme ve Politika Sürümü

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 16. günden devam
Geçici oturumun süresi henüz dolmamış olsa bile güvenlik nedeniyle **erken iptal** edilmesi gerekebilir.

**Revocation (iptal):** belirli oturuma erişim iznini geri almak.
**Policy version:** yetki kurallarının sürüm numarası. Yetkiler değişince eski sürümlü oturumları modelimiz reddeder.
**Fail closed:** yetki doğrulanamıyorsa izin verme.

Kod tenant, eylem, kaynak ve zaman denetimine ek olarak iptal edilmiş oturumları ve politika sürümünü kontrol eder.

## Çalıştır
```bash
python3 labs/17-session-revocation-and-policy-versioning/lab.py
python3 test_all.py
```

## Sorular
TTL ile revocation farkı nedir? Önbellekte eski politika kalırsa ne olabilir? Gerçek bulut sağlayıcılarında iptal neden her zaman anında uygulanmayabilir?

## Sınır
Gerçek oturum veya bulut sağlayıcı API'si kullanılmaz. Yalnızca yerel eğitim simülasyonudur.
