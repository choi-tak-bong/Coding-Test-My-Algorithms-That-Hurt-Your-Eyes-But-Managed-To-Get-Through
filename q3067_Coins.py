"""
https://www.acmicpc.net/problem/3067
"""

from sys import stdin
from typing import List

input = stdin.readline

t = int(input())

answers = [0] * t

def count_coins(n: int, coins: List[int], m: int):
    dp = [0] * (m + 1)
    
    for coin in coins:
        if coin > m:
            continue

        dp[coin] += 1

        for i in range(coin + 1, m + 1):
            dp[i] = dp[i] + dp[i-coin]

    return dp[-1]

for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    answers[i] = count_coins(n, coins, m)

print("\n".join(map(str, answers)))
