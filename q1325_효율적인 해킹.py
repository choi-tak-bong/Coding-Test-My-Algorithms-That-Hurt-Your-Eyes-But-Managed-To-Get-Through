"""
https://www.acmicpc.net/problem/1325
"""

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

max_value = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

def bfs(start: int):
    global max_value, n
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True
    result = 0

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                result += 1
                q.append(i)
                visited[i] = True
    max_value = max(max_value, result)
    return result

answers = [0] * (n + 1)

for i in range(1, n + 1):
    answers[i] = bfs(i)

for i in range(1, n + 1):
    if answers[i] == max_value:
        print(i, end=" ")