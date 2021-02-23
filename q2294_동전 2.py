"""
https://www.acmicpc.net/problem/q2294
"""

from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
dp = [1e9] * (k + 1)

for coin in coins:
    if coin > k:
        continue
    dp[coin] = 1
    for i in range(coin + 1, k + 1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[-1] if dp[-1] != 1e9 else -1)
