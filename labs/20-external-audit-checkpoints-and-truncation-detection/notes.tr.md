# Gün 20 — Harici Audit Checkpoint ve Log Sonunun Silinmesini Tespit

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 19. günden devam
Önceki gün **hash chain (özet zinciri)** ile kayıtların birbirine bağlanmasını öğrendik. Ama saldırgan tüm zinciri yeniden hesaplayabilir. Bu nedenle önceden kaydedilmiş, saldırganın değiştiremediği **harici checkpoint (kontrol noktası)** önemlidir.

Örnekte dört hayalî olay var. Güvenilen checkpoint `(kayıt sayısı, son hash)` içeriyor. Olay değiştirilirse veya son kayıt çıkarılırsa eski checkpoint eşleşmiyor. Ancak kötü niyetli kişi checkpoint'i de değiştirebilirse sahte veya eksik kayıtlar yeniden **geçerliymiş gibi** görünebilir.

**Trust boundary (güven sınırı):** logları değiştirebilen tarafın checkpoint'i değiştirememesi gerektiği alan ayrımı. Gerçek sistemde imzalı veya ayrı güvenli yerde tutulan kontrol noktaları gerekebilir.

## Çalıştırma
~~~bash
python3 labs/20-external-audit-checkpoints-and-truncation-detection/lab.py
python3 test_all.py
~~~

## Sorular
Checkpoint neden loglardan bağımsız saklanmalı? Zincirin doğru olması neden log içeriğinin gerçek olduğunu kanıtlamaz? Hiç yazılmamış bir olayı hash zinciri tespit edebilir mi?

## Sınırlar
Gerçek bulut logu, API, imza veya korumalı depolama yoktur; model yalnızca eğitim amaçlıdır.
