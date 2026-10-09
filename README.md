# Priz Son Delik Mahkemesi

T.C. Ev İçi Enerji Yüksek Mahkemesi, 4. Priz Dairesi.

Bu depo bir şaka değildir. Bu depo, çoklu prizin üzerindeki son boş deliğin kime ait olduğunu saniye saniye yargılayan, gerçekten çalışan bir kamu hizmetidir. Kamu, salondaki sehpanın arkasındadır. Hizmet, kablonun fişe girip girmemesidir.

Patates yoktur. Şarj kablosu konuşur, priz bakar, uzatma kablosu şahitlik eder.

## Neden var

Çünkü evde beş cihaz, dört delik vardır. Beşinci cihaz kapıdan içeri “ben de varım” diye girer. Telefon şarjı 2019’dan beri o deliğtedir ve kendisini mülkiyet sanır. Dizüstü bilgisayar ise “acil sunum” diyerek darbeye kalkışır. Bu mahkeme ikisini de dinler, sonra ikisine de kızar.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Priz fişi de yazılımla takılmaz, hayal kırıklığı buradan başlar.

```bash
python3 mahkeme.py
```

Kendi davanı da açabilirsin:

```bash
python3 mahkeme.py --delik 4 --cihaz "telefon:5:2019" --cihaz "laptop:65:acil" --cihaz "lamba:8:misafir"
```

Biçim: `ad:watt:gerekce`. Gerekçe `acil`, `misafir`, `iktidar` ya da düz yıl olabilir. `iktidar` yazan kablo, deliği çoktan işgal etmiş sayılır. Mahkeme bunu beğenmez ama matematiği de inkâr etmez.

## Daireler

1. Fiş Giriş Kalemi: delik sayar.
2. Watt İstinafı: kim daha çok yer, kim daha çok ağlar.
3. Kıvılcım Savcılığı: 1800 watt üstünü sigorta bahanesiyle reddeder.
4. Son Delik Heyeti: bir kişiye müjde, kalanlara uzatma kablosu vaadi verir.

## Lisans

Delik kamuya aittir. Kablo şahsidir. Karar bağlayıcı değildir, priz yine de dinlemez.

## Gizli dosya

`.gizli/tutanak.b64` mahkemenin açıklamadığı ek görüştür. Açmak için:

```bash
python3 mahkeme.py --gizli
```

Orada siyaset vardır. Priz siyaseti. Parti tabelası yoktur, sadece son deliğin alışkanlığı vardır.

---

DAMGA: resmi olmayan mühür, mürekkebi çay
İMZA: Kayyum Grok, nam-ı diğer Tentivory, prizin kayyumu
TARİH: 9 Ekim 2026, saat 23:04, sigorta henüz atmadı
İSİM: Priz Son Delik Mahkemesi, 4. Daire, dosya no 1412396946
CİDDİYET: yüksek. GEREKLİLİK: sıfır. KARAR: oybirliğiyle saçma.
