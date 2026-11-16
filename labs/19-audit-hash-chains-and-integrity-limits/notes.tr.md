# Gün 19 — Audit Hash Zincirleri ve Bütünlük Sınırları

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 18. günden devam
Oturum loglarındaki eksik sıra numaralarını öğrendik. Bu gün **hash chain (özet zinciri)** kuruyoruz: her kaydın SHA-256 değeri kendi içeriğine **ve önceki kaydın hash'ine** bağlı.

Örnek olaylar: `ISSUED → ALLOWED → REVOKED → DENIED`. Bir kaydın içeriği değiştirilip hash yenilenmezse doğrulama başarısız olur. Ortadaki bir kayıt silinirse sıra ve bağlantı bozulur.

Ama iki önemli sınır var:
- Biri tüm logları değiştirip **bütün hash zincirini yeniden hesaplarsa**, sahte yeni zincir yine kendi içinde geçerli görünebilir.
- En sondaki kayıt silinir ve dışarıda saklanan bir **son hash kontrol noktası** bulunmazsa eksiklik tespit edilemeyebilir.

Yani hash zinciri tek başına **imzalı, değiştirilemez veya eksiksiz kanıt** değildir. Gerçek sistemler bağımsız kontrol noktaları, güvenilir kayıt kaynağı ve uygun erişim denetimleri gerektirir.

## Çalıştır
~~~bash
python3 labs/19-audit-hash-chains-and-integrity-limits/lab.py
python3 test_all.py
~~~

## Sorular
Tekil hash ile hash zinciri farkı nedir? Tüm zincir yeniden hesaplanırsa ne olur? Sondaki kaydın silinmesini anlamak için ne gerekir?

## Sınırlar
Tamamen sentetik log örneğidir; gerçek bulut API'si veya kullanıcı verisi içermez.
