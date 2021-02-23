"""
https://www.acmicpc.net/problem/q2293
"""

from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)

for coin in coins:
    if coin > k:
        continue
    dp[coin] += 1
    for i in range(coin + 1, k + 1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[-1])

