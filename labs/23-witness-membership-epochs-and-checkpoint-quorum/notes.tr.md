# Gün 23 — Audit Tanık Üyeliği ve Policy Epoch

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 22. günden devam
Önceki gün **quorum (yeter sayı)** için iki farklı audit tanığının aynı checkpoint'i onaylamasını istedik. Peki bir tanığın yetkisi iptal edilirse?

**Witness membership:** güvenilen tanıkların listesi. **Policy epoch:** üye listesi değiştikçe artırılan sürüm. **Revocation:** artık güvenilmeyen bir tanığın oyunun kabul edilmemesi.

Başlangıçta tanıklar `a,b,c` ve epoch 1. Sonra aktif üyeler `b,c`, epoch 2 olur. Eski A tanığı artık sayılamaz. Hatta B'nin eski epoch 1 onayı da yeni quorum için geçerli değildir. Güncel epoch'tan iki farklı tanık gerekir.

## Çalıştır
```bash
python3 labs/23-witness-membership-epochs-and-checkpoint-quorum/lab.py
python3 test_all.py
```

## Sorular
Tanık üyeliği neden ayrıca doğrulanmalı? Eski onaylar neden güncel quorum'a katılamaz? HMAC anahtarı çalınırsa ne olur?

## Sınırlar
Gerçek bulut, dağıtık uzlaşı veya imzalama altyapısı kullanılmaz; yalnızca hayalî HMAC kayıtlarıdır.
