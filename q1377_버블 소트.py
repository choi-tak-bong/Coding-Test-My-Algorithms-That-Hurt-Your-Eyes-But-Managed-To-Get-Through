"""
https://www.acmicpc.net/problem/1377
"""

from sys import stdin

input = stdin.readline

n = int(input())
numbers = sorted([[int(input()), idx] for idx in range(n)])

max_idx_moving = 0

for i in range(len(numbers)):
    if (numbers[i][1] - i) >= max_idx_moving:
        max_idx_moving = numbers[i][1] - i

print(max_idx_moving + 1)
