"""
https://www.acmicpc.net/problem/1946
"""

import sys
from typing import List

input = sys.stdin.readline

t = int(input())
answer = []

def select_recruits(specs: List[List[int]]):
    specs.sort(key=lambda x: (x[0], x[1]))
    result = 0
    pre_1 = 1e9
    pre_2 = 1e9

    for spec in specs:
        if spec[0] > pre_1 and spec[1] > pre_2:
            continue
        pre_1, pre_2 = spec
        result += 1

    return result

for i in range(t):
    human_number = int(input())
    human_specs = [list(map(int, input().split())) for _ in range(human_number)]
    answer.append(select_recruits(human_specs))

print("\n".join(list(map(str, answer))))