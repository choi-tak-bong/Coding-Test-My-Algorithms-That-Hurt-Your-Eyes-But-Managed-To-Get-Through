"""
https://www.acmicpc.net/problem/status/14888
"""

from typing import List
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
plus_n, minus_n, multi_n, div_n = list(map(int, input().split()))
signs: List[str] = ["+"] * plus_n + ["-"] * minus_n + ["*"] * multi_n + ["//"] * div_n
sign_combination = list(set(permutations(signs, len(signs))))
answers: List[int] = []

for i in range(len(sign_combination)):
    copied_numbers = list(numbers)
    for j in range(len(sign_combination[i])):
        if sign_combination[i][j] == "//" and copied_numbers[j] < 0 and copied_numbers[j+1] > 0:
            copied_numbers[j+1] = -1 * (abs(copied_numbers[j]) // abs(copied_numbers[j+1]))
        else:
            copied_numbers[j+1] = eval(str(copied_numbers[j]) + sign_combination[i][j] + str(copied_numbers[j+1]))
    answers.append(copied_numbers[-1])

print(max(answers))
print(min(answers))