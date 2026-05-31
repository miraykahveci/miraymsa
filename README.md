# miraymsa

Dinamik programlama ile çoklu dizi hizalama (Multiple Sequence Alignment) kütüphanesi.

Bu kütüphane, **Needleman-Wunsch** algoritmasını ve onun **k boyuta genelleştirilmiş halini** kullanarak dizileri global olarak hizalar. Sum-of-Pairs (SP) skorlaması ile **optimal hizalamayı garanti eder** — Clustal Omega, MUSCLE veya MAFFT gibi heuristic yöntemlerin aksine yaklaşık değil, kesin sonuç verir.

## Özellikler

- **2 dizi için klasik Needleman-Wunsch** global hizalama
- **k dizi için saf dinamik programlama tabanlı MSA**
- Özelleştirilebilir match / mismatch / gap skorları
- Optimal Sum-of-Pairs skoru garanti
- İnteraktif komut satırı demosu

## Kurulum

```bash
git clone https://github.com/<miraykahveci>/miraymsa.git
cd miraymsa
pip install numpy
```

## Kullanım

### 2 dizi için (Needleman-Wunsch)

```python
from miraymsa import needleman_wunsch

h1, h2, skor = needleman_wunsch("GATTACA", "GCATGCU")
print(h1)    # GATTACA
print(h2)    # GCATGCU
print(skor)  # -1
```

### k dizi için (çoklu hizalama)

```python
from miraymsa import msa_align

hizalananlar, skor = msa_align(["GAT", "GCT", "GTT"])
for h in hizalananlar:
    print(h)
# GAT
# GCT
# GTT
print("Skor:", skor)  # 3
```

### Özelleştirilmiş skorlama parametreleriyle

```python
hizalananlar, skor = msa_align(
    ["ACGT", "AGT", "ACT"],
    match=2,
    mismatch=-1,
    gap=-2
)
```

### İnteraktif demo

```bash
python demo.py
```

Demo, kullanıcıdan dizi sayısını, dizileri ve skorlama parametrelerini alır.
2 dizi girilirse Needleman-Wunsch, 3+ dizi girilirse k boyutlu DP MSA kullanılır.

## Algoritma

### Needleman-Wunsch (2 dizi)

Klasik 2 boyutlu dinamik programlama rekürrensi

### k boyutlu DP (çoklu dizi)

k dizi için her hücrede `2^k - 1` yön ihtimali değerlendirilir. Sütun skoru, sütundaki tüm karakter çiftlerinin toplamıdır (Sum-of-Pairs)

### Karmaşıklık

| | Zaman | Bellek |
|---|---|---|
| 2 dizi NW | O(n·m) | O(n·m) |
| k dizi DP MSA | O(n^k · 2^k) | O(n^k) |

Saf DP MSA, küçük k değerleri için pratiktir. Bu doğal karmaşıklık sınırı, Clustal Omega, MUSCLE ve MAFFT gibi heuristic yöntemlerin geliştirilmesinin temel sebebidir.


## Testler

```bash
python -m tests.test_basic
```

Tüm test sonuçları doğrulanmıştır:
- Skorlama fonksiyonu: match, mismatch, gap
- 2 dizi Needleman-Wunsch: 3 örnek
- k dizi DP MSA: 3, 4 dizi örnekleri
- Tutarlılık testi: `msa_align(2 dizi)` = `needleman_wunsch(2 dizi)`

## Yazar

**Müzeyyen Miray Kahveci** — 231201047
Rumeli Üniversitesi, Bilgisayar Mühendisliği

Final projesi, Biyoinformatik dersi, 2025–2026 Bahar Dönemi.

