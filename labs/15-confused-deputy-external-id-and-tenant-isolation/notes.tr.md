# Gün 15 — Confused Deputy, External ID ve Bulutta Tenant İzolasyonu

[English](notes.md) · [Türkçe](notes.tr.md) · [Çevrimdışı Python uygulaması](lab.py)

## 14. günden devam
Önceki derste **rol güven politikası (trust policy)** ile **rolün sahip olduğu izinleri (permission policy)** ayırdık. Şimdi bir üçüncü taraf bulut servisinin birden fazla müşteriye hizmet verdiği durumları inceleyeceğiz.

Diyelim ki `tenant-a` ve `tenant-b`, aynı raporlama sağlayıcısına güveniyor. Sağlayıcı her müşterinin kendi raporunu okuyabiliyor. Ancak B'nin isteği yüzünden A'nın yetkileri kullanılırsa **confused deputy (yanıltılan yetkili aracı)** problemi doğabilir: kendi yetkileri olan bir servis yanlış taraf adına işlem yapar.

## Birbirinden farklı üç koruma
1. **Çağıranı doğrulama:** Gerçek bulut sisteminde servis kimliği güvenilir kimlik doğrulama mekanizmalarıyla onaylanmalı. Bu lab'de `principal` bilgisinin önceden doğrulandığını **varsayıyoruz**; kod oturum açma yapmıyor.
2. **İsteği doğru tenant'a bağlama:** AWS'nin üçüncü taraf entegrasyonlarında kullanılabilen `ExternalId` koşulu, confused deputy riskini azaltmaya yardımcı olabilir. Burada her tenant için farklı, **uydurma bir referans değeri** var. External ID **parola veya gizli bir kimlik doğrulama anahtarı değildir**. Asıl mesele iş ortağının gelen isteği gerçekten doğru müşteriye bağlamasıdır.
3. **İzinleri en aza indirme:** Rol varsayımı başarılı olsa bile o oturum yalnızca gerekli işleme ve müşterinin kaynağına erişebilmelidir. Örneğimizde sadece kendi `report:quarterly` raporunu `read` izni vardır. Silme veya başka tenant'ın raporunu okuma reddedilir.

Önemli: Güven kontrolü ile kaynak yetkilendirmesi **ayrı aşamalardır**. Bir External ID'nin eşleşmesi, kullanıcıya sınırsız yetki vermez. Gerçek sistemlerde açık ret kuralları, kaynak politikaları, organizasyon politikaları, oturum koşulları ve denetim kayıtları da değerlendirilmelidir.

## Uygulama
```bash
python lab.py
```
Bulut hesabı, API anahtarı, internet ve ücretli hizmet gerekmiyor. Python standart kütüphanesiyle **7 sentetik vaka** sınanır:
- Doğru tenant-a ve tenant-b oturumları kendi raporlarını okuyabilir.
- Yanlış External ID, tanınmayan kimlik ve tanınmayan tenant reddedilir.
- A'nın geçerli oturumu, B'nin raporuna erişemez veya kendi raporunu silemez.

Kod `AssumeRequest → Session → resource authorization` aşamalarını modeller. Gerçek bir rol oluşturmaz veya veri göndermez.

## Görevler
1. Rolü üstlenmeye güven duyulan servis, neden tüm kaynakları otomatik kullanamaz?
2. Tenant B'ye ait referans A'ya ait istek için kullanılırsa hangi denetim devreye girer?
3. External ID'yi şifre gibi değerlendirmek neden yanlıştır? Entegrasyonu yürüten servisin müşteriyi nasıl doğrulaması gerekir?
4. A'ya ikinci bir rapor ekle; B'nin erişim izni neden değişmemeli?
5. Denetim kaydı için principal, tenant, işlem, kaynak, karar ve correlation ID alanlarını nasıl seçersin?
6. Bu oyuncak modelin gerçek AWS IAM semantiğinde bulunmayan veya eksik bıraktığı hangi denetimler var?

## Güvenlik ve kaynaklar
Bu bir **AWS kavramlarından esinlenmiş eğitim modeli**dir; gerçek IAM policy motoru değildir. Sağlayıcı farkları ve gerçek trust/federation kuralları ayrıca incelenmelidir.
- [AWS: External ID ve confused deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html)
- [AWS: IAM rolleri](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

Gerçek kaynakları yalnızca yetkili olduğun ortamlarda incele.
