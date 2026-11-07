# Gün 05 — VPC, Alt Ağlar ve Güvenlik Grubu Kuralları

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical lab](lab.py)

## Öğrenme hedefi

Bulutta ağ segmentasyonu, servislerin birbirine hangi yollarla erişebileceğini sınırlar. Alt ağ rotası, güvenlik grubu kuralı ve uygulama yetkilendirmesi farklı güven sınırlarını korur.

## Temel kavramlar ve güven sınırları

1. CIDR, IP adres aralığıdır; kullanıcı kimliği değildir. Sadece ağ konumuna bakarak yetkilendirme yapılmaz.

2. Giriş kuralı protokol, port ve sınırlandırılmış kaynak içerir; 0.0.0.0/0 tüm IPv4 kaynaklarını ifade eder.

3. Bulut sağlayıcıların stateful/stateless ve kural sırası semantiği değişebilir. Bu örnek basit izin eşleme modeli kullanır.

## Örnek senaryo

Dahili API yalnız 10.1.0.0/16 aralığından HTTPS kabul etmeli, internetten rastgele istemcileri ve SSH isteğini reddetmeli.

## Yerel uygulama

Bu klasördeki `lab.py` dosyasını önce oku, ardından Python 3 ile çalıştır:

```bash
python lab.py
```

Kod yalnız sentetik veri ve Python standart kütüphanesi kullanır. Her güvenlik kararı otomatik `assert` kontrolleriyle örneklenir.

## Görevler

1. 10.1.2.3:443 erişimini ve 203.0.113.5:443 reddini doğrula.
2. İç ağdan 22 portunu dene.
3. Modelin rotaları ve dönüş trafiğini neden temsil etmediğini yaz.

## Değerlendirme soruları

1. Girdi ve verinin sahibi kim? Hangi alanlar güvenilir sayılmamalı?
2. Programın doğrudan gözlemi ile senin yorumunu ayır.
3. Olumsuz durum / yanlış pozitif örneği ekle ve nedenini açıkla.
4. Bu sentetik modelin gerçek bulut sağlayıcısından farkı nedir?

## Güvenlik, etik ve sınırlamalar

Canlı hesap, gerçek kimlik bilgisi, ücretli servis veya dış hedef gerekmez. Bu sonuçlar gerçek ortamın güvenli olduğunu **kanıtlamaz**. Üretim ortamındaki kurallar sağlayıcı belgeleri ve yetkili testlerle doğrulanmalıdır.

## Önerilen kaynaklar

- [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [CISA Cloud Security](https://www.cisa.gov/topics/cybersecurity-best-practices/cloud-security)
