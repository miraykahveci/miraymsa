"""
miraymsa - Dinamik Programlama ile Çoklu Dizi Hizalama Kütüphanesi.

Bu kütüphane, Needleman-Wunsch algoritmasını ve onun k boyuta
genelleştirilmiş halini kullanarak dizileri global olarak hizalar.
Sum-of-Pairs (SP) skorlaması ile optimal hizalama garanti edilir.

Kullanım:
    from miraymsa import needleman_wunsch, msa_align

    # 2 dizi için klasik Needleman-Wunsch
    h1, h2, skor = needleman_wunsch("GATTACA", "GCATGCU")

    # k dizi için çoklu hizalama
    hizalananlar, skor = msa_align(["GAT", "GCT", "GTT"])

Yazar: Müzeyyen Miray Kahveci (231201047)
Algoritma: Dinamik Programlama
"""

from .dp_align import needleman_wunsch
from .msa import msa_align, sum_of_pairs
from .scoring import simple_score

__version__ = "0.1.0"
__author__ = "Müzeyyen Miray Kahveci"
__all__ = [
    "needleman_wunsch",
    "msa_align",
    "sum_of_pairs",
    "simple_score",
]