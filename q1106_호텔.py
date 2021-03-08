"""
https://www.acmicpc.net/problem/1106
"""

from sys import stdin

input = stdin.readline

INF = 1e9
MAX = 1101

c, n = map(int, input().split())

infos = [list(map(int, input().split())) for _ in range(n)]
dp = [INF] * MAX

for info in infos:
    money, human = info

    for i in range(1, human + 1):
        dp[i] = min(dp[i], money)

    for i in range(human + 1, c + 1):
        dp[i] = min(dp[i], dp[i-human] + money)

print(dp[c])
