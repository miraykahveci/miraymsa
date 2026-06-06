"""
2 dizi için Needleman-Wunsch algoritması — global hizalama.
Bu modül, klasik dinamik programlama yöntemiyle iki diziyi global olarak
hizalar. 

Karmaşıklık: O(n*m) zaman, O(n*m) bellek 
"""

from .scoring import simple_score

CAPRAZ = 1   
YUKARI = 2  
SOL = 3      

def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
   
    n = len(seq1)
    m = len(seq2)

    F = [[0] * (m + 1) for _ in range(n + 1)]
    P = [[0] * (m + 1) for _ in range(n + 1)]

    # ADIM 1: İlk satır ve sütunu doldur
    for j in range(1, m + 1):
        F[0][j] = F[0][j - 1] + gap
        P[0][j] = SOL

    for i in range(1, n + 1):
        F[i][0] = F[i - 1][0] + gap
        P[i][0] = YUKARI

    # ADIM 2: Matrisi doldur 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            capraz_skor = F[i - 1][j - 1] + simple_score(
                seq1[i - 1], seq2[j - 1], match, mismatch, gap
            )
            yukari_skor = F[i - 1][j] + gap
            sol_skor    = F[i][j - 1] + gap

            en_iyi = max(capraz_skor, yukari_skor, sol_skor)
            F[i][j] = en_iyi

            if en_iyi == capraz_skor:
                P[i][j] = CAPRAZ
            elif en_iyi == yukari_skor:
                P[i][j] = YUKARI
            else:
                P[i][j] = SOL

    # ADIM 3: Traceback 
    hizalanan1 = []
    hizalanan2 = []
    i, j = n, m

    while i > 0 or j > 0:
        if P[i][j] == CAPRAZ:
            hizalanan1.append(seq1[i - 1])
            hizalanan2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif P[i][j] == YUKARI:
            hizalanan1.append(seq1[i - 1])
            hizalanan2.append('-')
            i -= 1
        else:  # SOL
            hizalanan1.append('-')
            hizalanan2.append(seq2[j - 1])
            j -= 1

    hizalanan1 = ''.join(reversed(hizalanan1))
    hizalanan2 = ''.join(reversed(hizalanan2))

    return hizalanan1, hizalanan2, F[n][m]
