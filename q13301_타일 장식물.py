"""
https://www.acmicpc.net/problem/q13301
"""

from sys import stdin

input = stdin.readline

n = int(input()) - 1

dp_l = [1, 2] + [1] * 78
dp_s = [1, 1] + [1] * 78

for i in range(2, 80):
    dp_l[i] = dp_l[i-1] + dp_l[i-2]
    dp_s[i] = dp_s[i-1] + dp_s[i-2]

print(dp_l[n] * 2 + dp_s[n] * 2)