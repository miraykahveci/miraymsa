from miraymsa.dp_align import needleman_wunsch
from miraymsa.scoring import simple_score
from miraymsa.msa import msa_align


print("=" * 50)
print("SKORLAMA TESTLERİ")
print("=" * 50)

print("simple_score('A','A') =", simple_score('A', 'A'))   # 1
print("simple_score('A','G') =", simple_score('A', 'G'))   # -1
print("simple_score('A','-') =", simple_score('A', '-'))   # -2


print()
print("=" * 50)
print("NEEDLEMAN-WUNSCH TESTLERİ (2 dizi)")
print("=" * 50)

# Test 1:
print("\nTest 1: GAT vs GCT")
h1, h2, skor = needleman_wunsch("GAT", "GCT")
print(h1)
print(h2)
print("Skor:", skor)

# Test 2:
print("\nTest 2: GATTACA vs GCATGCU")
h1, h2, skor = needleman_wunsch("GATTACA", "GCATGCU")
print(h1)
print(h2)
print("Skor:", skor)

# Test 3: 
print("\nTest 3: SEND vs AND")
h1, h2, skor = needleman_wunsch("SEND", "AND")
print(h1)
print(h2)
print("Skor:", skor)


print()
print("=" * 50)
print("MSA TESTLERİ (k dizi için)")
print("=" * 50)

# Test 1: 3 dizi
print("\nTest 1: 3 dizi (GAT, GCT, GTT)")
hizalananlar, skor = msa_align(["GAT", "GCT", "GTT"])
for h in hizalananlar:
    print(h)
print("Skor:", skor)

# Test 2: 
print("\nTest 2: 4 dizi (ACGT, AGT, ACT, ACGT)")
hizalananlar, skor = msa_align(["ACGT", "AGT", "ACT", "ACGT"])
for h in hizalananlar:
    print(h)
print("Skor:", skor)

# Test 3: msa_align ile 2 dizi de çalışıyor mu? (özel durum olarak)
# Bu test, k dizi DP'nin 2 dizi NW ile aynı sonucu verdiğini kanıtlar
print("\nTest 3: 2 dizi (msa_align ile) - GAT vs GCT")
hizalananlar, skor = msa_align(["GAT", "GCT"])
for h in hizalananlar:
    print(h)
print("Skor:", skor)
print("(Bu skor yukarıdaki NW Test 1 ile aynı olmalı: 1)")