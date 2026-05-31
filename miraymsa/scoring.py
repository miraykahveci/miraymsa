"""
Skorlama fonksiyonları.

Bu modül, iki karakter (nükleotid, amino asit veya gap) arasındaki
benzerliği sayısal bir skora çeviren fonksiyonu içerir.
"""


def simple_score(a, b, match=1, mismatch=-1, gap=-2):
    if a == '-' or b == '-':
        return gap
    elif a == b:
        return match
    else:
        return mismatch