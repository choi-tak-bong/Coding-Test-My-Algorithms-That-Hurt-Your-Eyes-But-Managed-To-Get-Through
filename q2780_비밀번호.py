"""
https://www.acmicpc.net/problem/q2087
"""

from sys import stdin

input = stdin.readline

t = int(input())
answers = [0] * t
touch_pad = [
    [7],
    [2, 4],
    [1, 3, 5],
    [2, 6],
    [1, 5, 7],
    [2, 4, 6, 8],
    [3, 5, 9],
    [0, 4, 8],
    [5, 7, 9],
    [6, 8]
]

dp = [([0] * 10) for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, 1001):
    for j in range(10):
        dp[i][j] = sum([dp[i-1][touch_pad[j][v]] for v in range(len(touch_pad[j]))])
        dp[i][j] = dp[i][j] % 1234567

for i in range(t):
    n = int(input())

    for j in range(10):
        answers[i] += dp[n][j]
    answers[i] = answers[i] % 1234567

print("\n".join(map(str, answers)))
