# Gün 18 — Oturum Denetim Logları ve Eksik Olay Kanıtları

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 17. günden devam
Önceki gün oturum iptali ve politika sürümünü gördük. Bu kez işlem sonrasında elde kalan **audit trail (denetim izi)** kayıtlarını inceliyoruz.

Hayalî olay sırası: `ISSUED` (oturum verildi), `ALLOWED_WHILE_ACTIVE` (aktifken izin verildi), `REVOKED` (iptal edildi) ve `DENIED_REVOKED` (iptal nedeniyle reddedildi).

**Sequence number (sıra numarası):** kayıtların sırasını izlemek için kullanılan sayı. **Gap (boşluk):** aradan bir olayın kaybolmuş veya aktarılmamış olabileceğine işaret eden sıçrama. Ancak gap olmaması logların tam ve değiştirilmemiş olduğunu **kanıtlamaz**.

Kod eksik kayıt, tekrar numarası, ters sıra, iptalden sonra izin ve bilinmeyen olayları test eder.

## Çalıştırma
~~~bash
python3 labs/18-session-audit-sequences-and-missing-event-evidence/lab.py
python3 test_all.py
~~~

## Sorular
Eksik sıra numarası neden önemlidir? Bütün numaraları yeniden yazan biri tespiti nasıl yanıltabilir? Gerçek bulut sistemlerinde olaylar neden gecikmeli gelebilir?

## Sınır
Gerçek bulut sağlayıcısı veya log incelenmez. Bu model tamper-proof kayıt veya kesin aktör atfı sağlamaz.
