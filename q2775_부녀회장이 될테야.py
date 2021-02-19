"""
https://www.acmicpc.net/problem/2775
"""

import sys

input = sys.stdin.readline

t = int(input())
dp = [list(range(1, 15))] + [[1] for _ in range(14)]

for i in range(14):
    for j in range(1, 14):
        dp[i+1].append(dp[i+1][j-1] + dp[i][j])

answer = []

for i in range(t):
    k = int(input())
    n = int(input())
    answer.append(dp[k][n-1])

print("\n".join(list(map(str, answer))))