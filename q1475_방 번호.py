"""
https://www.acmicpc.net/problem/1475
"""

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = sorted(list(input()))
dp = [0] * 10

for i in range(10):
    dp[i] = bisect_right(n, str(i)) - bisect_left(n, str(i))

dp[9] += dp[6]
dp[6] = 0

if dp[9] % 2 == 0:
    dp[9] //= 2
else:
    dp[9] = dp[9] // 2 + 1

print(max(dp))