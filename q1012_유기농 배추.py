"""
https://www.acmicpc.net/problem/1012
"""

from sys import stdin, setrecursionlimit
from typing import List
from collections import deque

input = stdin.readline
setrecursionlimit(1000000)

t = int(input())

answers = [0] * t

def check_baechoo_bfs(x: int, y: int):
    global m, n, k, field, visited
    
    if x < 0 or y < 0 or x > m - 1 or y > n - 1:
        return

    if field[y][x] == 0:
        return

    if visited[y][x]:
        return

    visited[y][x] = True

    check_baechoo_bfs(x - 1, y)
    check_baechoo_bfs(x + 1, y)
    check_baechoo_bfs(x, y - 1)
    check_baechoo_bfs(x, y + 1)

for tc in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] == 1:
                count += 1
                check_baechoo_bfs(j, i)

    answers[tc] = count

print("\n".join(map(str, answers)))