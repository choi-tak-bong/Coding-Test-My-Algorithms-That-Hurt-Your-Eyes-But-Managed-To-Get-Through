"""
https://www.acmicpc.net/problem/q1174
"""

from itertools import combinations
from sys import stdin

input = stdin.readline

n = int(input())

numbers = [i for i in range(10)]
combis = []

for i in range(1, 11):
    temp_combi = list(combinations(numbers, i))
    for j in range(len(temp_combi)):
        sorted_list = sorted(temp_combi[j])
        tmp = 0
        for k in range(i):
            tmp += (10 ** k) * sorted_list[k]
        combis.append(tmp)

combis.sort()

print(-1 if n > 1023 else combis[n-1])