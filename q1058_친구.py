"""
https://www.acmicpc.net/problem/1058
"""

from sys import stdin

INF = 1e9

input = stdin.readline

n = int(input())

dp = [[INF] * n for _ in range(n)]
string = []

for i in range(n):
    string.append(list(input()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if string[i][j] == "Y" or (string[i][k] == "Y" and string[k][j] == "Y"):
                dp[i][j] = 1

result = 0

for i in range(n):
    c = 0
    for j in range(n):
        if dp[i][j] == 1:
            c += 1
    result = max(result, c)

print(result)