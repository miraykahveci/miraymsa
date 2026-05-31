"""
k dizi için Dinamik Programlama tabanlı çoklu dizi hizalama.

Needleman-Wunsch algoritmasının k boyuta genelleştirilmiş halidir.
Sum-of-Pairs (SP) skorlama kullanır.

Karmaşıklık: O(n^k * 2^k) zaman, O(n^k) bellek
n: dizi uzunluğu, k: dizi sayısı
"""

import numpy as np
from itertools import product
from .scoring import simple_score


def sum_of_pairs(karakterler, match=1, mismatch=-1, gap=-2):
    toplam = 0
    n = len(karakterler)
    for a in range(n):
        for b in range(a + 1, n):
            toplam += simple_score(karakterler[a], karakterler[b],
                                   match, mismatch, gap)
    return toplam


def msa_align(diziler, match=1, mismatch=-1, gap=-2):
  
    k = len(diziler)
    if k < 2:
        raise ValueError("En az 2 dizi gerekli")

    boyutlar = tuple(len(d) + 1 for d in diziler)

    F = np.zeros(boyutlar, dtype=int)
    P = np.full(boyutlar, -1, dtype=int)

    hareketler = [h for h in product([0, 1], repeat=k) if any(h)]


    for hucre in np.ndindex(boyutlar):
        if all(x == 0 for x in hucre):
            continue

        en_iyi_skor = None
        en_iyi_hareket = -1

        for h_idx, hareket in enumerate(hareketler):
            onceki = tuple(hucre[i] - hareket[i] for i in range(k))

            if any(x < 0 for x in onceki):
                continue
            
            sutun = []
            for i in range(k):
                if hareket[i] == 1:
                    sutun.append(diziler[i][hucre[i] - 1])
                else:
                    
                    sutun.append('-')

            yeni_skor = F[onceki] + sum_of_pairs(sutun, match, mismatch, gap)

            if en_iyi_skor is None or yeni_skor > en_iyi_skor:
                en_iyi_skor = yeni_skor
                en_iyi_hareket = h_idx

        F[hucre] = en_iyi_skor
        P[hucre] = en_iyi_hareket

    # ---- Traceback ----
    hizalananlar = [[] for _ in range(k)]
    hucre = tuple(len(d) for d in diziler)  

    while any(x > 0 for x in hucre):
        h_idx = P[hucre]
        hareket = hareketler[h_idx]

        for i in range(k):
            if hareket[i] == 1:
                hizalananlar[i].append(diziler[i][hucre[i] - 1])
            else:
                hizalananlar[i].append('-')

        hucre = tuple(hucre[i] - hareket[i] for i in range(k))

    hizalananlar = [''.join(reversed(h)) for h in hizalananlar]

    son_hucre = tuple(len(d) for d in diziler)
    return hizalananlar, int(F[son_hucre])