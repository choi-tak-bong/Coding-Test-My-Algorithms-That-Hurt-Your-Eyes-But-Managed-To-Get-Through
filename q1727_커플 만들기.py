"""
https://www.acmicpc.net/problem/3067
"""

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

jujis = sorted(list(map(int, input().split())))
bujis = sorted(list(map(int, input().split())))

dp = [[0] * (1001) for _ in range(1001)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + abs(jujis[i-1] - bujis[j-1])
        elif i > j:
            dp[i][j] = min(dp[i-1][j-1] + abs(jujis[i-1] - bujis[j-1]), dp[i-1][j])
        elif i < j:
            dp[i][j] = min(dp[i-1][j-1] + abs(jujis[i-1] - bujis[j-1]), dp[i][j-1])

print(dp[n][m])
