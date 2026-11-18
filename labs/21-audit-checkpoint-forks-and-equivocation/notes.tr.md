# Gün 21 — Audit Checkpoint Çatallanması ve Farklı Geçmiş Sunma

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 20. günden devam
Önceki gün harici checkpoint ile değiştirilmiş veya kısaltılmış logları karşılaştırdık. Bugün daha ilginç bir sorun var: bir sistem aynı uzunlukta fakat **birbirini tutmayan iki log geçmişi** sunarsa ne olur?

**Fork (çatallanma):** ortak başlangıçtan sonra iki farklı olay zincirinin oluşması. **Equivocation / split view:** farklı gözlemcilere çelişkili geçmişler gösterilmesi. **Checkpoint:** olay sayısı ve son hash gibi özet bilgiler.

Kod iki hayalî logu karşılaştırır. Sayıları aynı ama hash'leri farklıysa `CONFLICTING_CHECKPOINTS`; sayıları farklıysa `DIFFERENT_HEIGHTS`; ikisi de eşitse `CONSISTENT_AT_HEIGHT` der.

**Önemli:** farklı hash görmek hangi logun doğru olduğunu tek başına söylemez. Kayıtları bağımsız ve doğrulanabilir biçimde saklayan gözlemciler gerekir.

## Çalıştır
~~~bash
python3 labs/21-audit-checkpoint-forks-and-equivocation/lab.py
python3 test_all.py
~~~

## Sorular
İki log neden aynı sayıda olay içerip farklı olabilir? Bağımsız denetçiler neden önemli? Geçerli hash olayların gerçek olduğunu kanıtlar mı?

## Sınır
Gerçek cloud audit log veya imzalı checkpoint kullanılmaz; yalnızca yerel sentetik veridir.
