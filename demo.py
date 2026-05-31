"""
miraymsa - İnteraktif çoklu dizi hizalama demosu.
Kullanıcıdan k tane dizi alır ve dinamik programlama ile hizalar.

2 dizi için klasik Needleman-Wunsch (dp_align.py) kullanılır.
3 veya daha fazla dizi için k boyutlu DP MSA (msa.py) kullanılır.
"""

from miraymsa.msa import msa_align
from miraymsa.dp_align import needleman_wunsch


def yazdir_hizalamayi(hizalananlar):
    k = len(hizalananlar)
    uzunluk = len(hizalananlar[0])

    esles = []
    for j in range(uzunluk):
        sutun = [hizalananlar[i][j] for i in range(k)]
        if all(c == sutun[0] for c in sutun) and sutun[0] != '-':
            esles.append('|')
        else:
            esles.append(' ')
    esles_str = ''.join(esles)

    for i, h in enumerate(hizalananlar, start=1):
        print(f"Dizi {i}: {h}")
    print(f"       {esles_str}")


def main():
    print("=" * 60)
    print("  miraymsa - DİNAMİK PROGRAMLAMA İLE ÇOKLU DİZİ HİZALAMA")
    print("=" * 60)

    # ---- Dizi sayısı ----
    while True:
        try:
            k = int(input("\nKaç dizi hizalanacak? (en az 2): ").strip())
            if k >= 2:
                break
            print("En az 2 dizi girmelisin.")
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")

    if k >= 5:
        print(f"\n⚠️  Uyarı: {k} dizi için karmaşıklık O(n^{k}) — uzun diziler "
              f"hesaplamayı çok yavaşlatabilir. Kısa diziler tavsiye edilir.")

    
    diziler = []
    for i in range(1, k + 1):
        while True:
            dizi = input(f"Dizi {i}: ").strip().upper()
            if dizi:
                diziler.append(dizi)
                break
            print("Boş dizi olamaz, tekrar gir.")

    
    print("\nSkorlama parametreleri (varsayılan için Enter'a bas):")
    match_in = input("  Match skoru     [varsayılan 1]:  ").strip()
    mismatch_in = input("  Mismatch skoru  [varsayılan -1]: ").strip()
    gap_in = input("  Gap cezası      [varsayılan -2]: ").strip()

    match = int(match_in) if match_in else 1
    mismatch = int(mismatch_in) if mismatch_in else -1
    gap = int(gap_in) if gap_in else -2

   
    print("\nHesaplanıyor...")
    if len(diziler) == 2:
        print("(2 dizi → Needleman-Wunsch kullanılıyor)")
        h1, h2, skor = needleman_wunsch(diziler[0], diziler[1],
                                        match, mismatch, gap)
        hizalananlar = [h1, h2]
    else:
        print(f"({len(diziler)} dizi → k boyutlu DP MSA kullanılıyor)")
        hizalananlar, skor = msa_align(diziler, match, mismatch, gap)

    print("\n" + "=" * 60)
    print("SONUÇ")
    print("=" * 60)
    yazdir_hizalamayi(hizalananlar)
    print(f"\nSkor:              {skor}")
    print(f"Hizalama uzunluğu: {len(hizalananlar[0])}")


if __name__ == "__main__":
    main()