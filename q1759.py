"""
https://www.acmicpc.net/problem/1759
"""

from itertools import combinations

l, c = map(int, input().split())
texts = list(input().split())
texts.sort()

vowels = ("a", "e", "i", "o", "u")

for text_combi in combinations(texts, l):
    consonant_num = 0
    vowel_num = 0
    
    for i in range(len(text_combi)):
        if text_combi[i] in vowels:
            vowel_num += 1
        else:
            consonant_num += 1

    if consonant_num >= 2 and vowel_num >= 1:
        print("".join(text_combi))
