"""
https://www.acmicpc.net/problem/q15651
"""

from itertools import product
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

answers = list(product(list(range(1, n + 1)), repeat=m))

for i in range(len(answers)):
    print(" ".join(list(map(str, answers[i]))))