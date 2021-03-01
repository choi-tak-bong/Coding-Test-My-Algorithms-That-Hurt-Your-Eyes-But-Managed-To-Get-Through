"""
https://www.acmicpc.net/problem/q1038
"""

from itertools import combinations
from sys import stdin

input = stdin.readline

n = int(input())
n += 1

numbers = [i for i in range(10)]
combis = []

for i in range(1, 11):
    temp_combi = list(combinations(numbers, i))
    for j in range(len(temp_combi)):
        sorted_list = sorted(temp_combi[j])
        temp = 0
        for k in range(i):
            temp += (10 ** k) * sorted_list[k]
        combis.append(temp)

combis.sort()
print(-1 if n > 1023 else combis[n-1])
