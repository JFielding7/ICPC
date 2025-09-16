from collections import defaultdict


def valid_translation(a, b, translations, tried):
    if a == b:
        return True
    if a in tried:
        return False

    tried.add(a)
    return b in translations[a] or any(valid_translation(c, b, translations, tried) for c in translations[a])


def secret_chamber():
    m, n = tuple(map(int, input().split()))
    translations = defaultdict(set)

    for _ in range(m):
        a, b = tuple(input().split())
        translations[a].add(b)

    for _ in range(n):
        word0, word1 = tuple(input().split())
        print("yes" if len(word0) == len(word1) and all(valid_translation(a, b, translations, set()) for a, b in zip(word0, word1)) else "no")


secret_chamber()
