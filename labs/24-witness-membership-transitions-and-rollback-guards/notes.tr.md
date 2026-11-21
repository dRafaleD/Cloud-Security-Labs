# Gün 24 — Audit Tanık Üyeliği Değişikliği ve Rollback Koruması

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 23. günden devam
Önceki gün hangi tanığın güncel epoch içinde yetkili olduğunu kontrol ettik. Şimdi **tanık listesini güvenli biçimde değiştirmeyi** modelliyoruz.

**Membership transition:** tanık kümesinin yeni sürüme geçmesi. **Epoch:** politika sürümü. **Rollback:** eski politika sürümünü yeniden yürürlüğe sokma. **Quorum:** yeterli sayıda farklı tanığın onayı.

Bu örnekte bir geçiş için mevcut tanıklardan **iki farklı HMAC onayı** gerekiyor. Onay, eski/yeni epoch numarasını ve yeni üye listesini kapsıyor. Aynı onayın iki kez gelmesi, geçersiz HMAC, eski epoch veya emekliye ayrılmış tanığın imzası yeterli sayılmıyor.

## Çalıştırma
```bash
python3 labs/24-witness-membership-transitions-and-rollback-guards/lab.py
python3 test_all.py
```

## Sorular
Onay neden tüm üye listesine bağlanmalı? Eski sürüm onayı neden tekrar kullanılmamalı? Güvenilen politika kaydı geri alınabiliyorsa hangi sorun doğar?

## Sınırlar
Gerçek dağıtık uzlaşı, bulut API veya güvenli imza altyapısı değildir; yalnızca hayalî HMAC ve bellek kayıtlarıdır.
