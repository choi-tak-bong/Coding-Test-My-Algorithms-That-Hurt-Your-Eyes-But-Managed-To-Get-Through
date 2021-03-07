"""
https://www.acmicpc.net/problem/11404
"""

from sys import stdin

input = stdin.readline

INF = 1e9

n, m = int(input()), int(input())

cost = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(n):
    for j in range(n):
        if cost[i][j] == INF:
            print(0, end=" ")
            continue
        print(cost[i][j], end=" ")
    print("")
