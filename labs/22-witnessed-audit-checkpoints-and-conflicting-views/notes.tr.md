# Gün 22 — Tanıklı Audit Checkpoint ve Çelişkili Görünümler

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lab.py)

## 21. günden devam
Önceki gün aynı uzunlukta ama hash'i farklı iki log geçmişi gördük. Şimdi bağımsız kaynakların **checkpoint tanıklığını** simüle ediyoruz.

**Witness (tanık):** bir checkpoint hakkında doğrulanabilir görüş bildiren kaynak. **Attestation (onay kaydı):** tanığın belirli yükseklik ve hash için oluşturduğu doğrulama verisi. **Quorum (yeter sayı):** karar için gereken farklı tanık sayısı.

Üç hayalî tanıktan en az ikisi aynı `(kayıt sayısı, hash)` değerini doğrularsa **QUORUM** oluşur. Bir tanığın aynı checkpoint'i iki kez göndermesi iki oy sayılmaz. Aynı yükseklikte farklı hash görünürse **CONFLICTING_VIEWS** olur; aynı tanık iki farklı hash'i onaylarsa **WITNESS_EQUIVOCATION** olarak işaretlenir.

## Çalıştır
```bash
python3 labs/22-witnessed-audit-checkpoints-and-conflicting-views/lab.py
python3 test_all.py
```

## Sorular
Kopyalanan onay neden yeni tanık sayılmaz? Farklı yükseklikteki checkpoint neden doğrudan çatallanma kanıtı değildir? Anahtar sızıntısı sistemi nasıl etkiler?

## Sınır
Gerçek bulut, gerçek denetçi veya kriptografik imza sistemi yoktur. HMAC anahtarları eğitim değerleridir.
