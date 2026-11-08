# Gün 14 — Hesaplar Arası Rol Güveni ve İzin Kapsamı

[English](notes.md) · [Türkçe](notes.tr.md) · [Çevrimdışı uygulama](lab.py)

## Neden iki ayrı kontrol gerekiyor?
Bulut ortamlarında farklı ekipler ve iş yükleri ayrı hesap, proje veya aboneliklerde bulunabilir. Bir kimliğin başka bir hesaptaki rolü üstlenmesine **güven duymak**, o role **her kaynağa sınırsız erişim vermek** anlamına gelmez.

## Birbirinden farklı iki soru
1. **Rolü kim üstlenebilir?** Trust/federation politikası güvenilen kimlikleri tanımlar. Gerçek sistemlerde hesap kimliği, kimlik sağlayıcı, audience, koşullar ve external ID gibi alanlar önem kazanabilir.
2. **Rolü üstlenen ne yapabilir?** Permission politikası eylem ve kaynakları kısıtlar. Güvenilen kimliğe de yalnız gerekli **en az yetki** verilmelidir.

Aşırı geniş trust politikası istenmeyen kimlikleri içeri alır. Dar permission etkisini azaltabilir ama ilk sorunu tamamen çözmez. Tersine, doğru trust kurulması da aşırı yetkili rolü güvenli yapmaz. Gerçek sistemler ayrıca açık ret, session, organizasyon politikası ve kaynak politikaları uygular.

## Yerel uygulama
```bash
python lab.py
```
Uygulama **uydurma** `tenant-a:reporter` ve `report:quarterly` kimliklerini kullanır. Sadece ilgili rapora okuma izni verir; güvenilmeyen kimliği, silmeyi ve farklı kaynağı reddeder. **Bulut API çağrısı veya credential gerekmez.**

## Görevler
1. Beş testin sonucunu önceden tahmin et.
2. Güvenilen kimlikler arasına `tenant-b:analyst` ekle; bu değişiklik otomatik export izni sağlar mı?
3. Çalınan kimlik bilgisi ile aşırı geniş trust politikasının risklerini ayır.
4. Rol üstlenme, ret ve kaynak erişimini izleyecek log alanları tasarla.
5. Gerçek AWS/Azure/GCP ortamına uyarlamadan önce hangi sağlayıcı özellikleri doğrulanmalı?

## Güvenlik ve sınırlamalar
Kod **politikaların birleşimini** anlatır; gerçek IAM karar motoru veya üretim güvenliği kanıtı değildir. Gerçek deneme yalnız yetkili ortam ve güncel sağlayıcı dokümantasyonuyla yapılmalıdır.
