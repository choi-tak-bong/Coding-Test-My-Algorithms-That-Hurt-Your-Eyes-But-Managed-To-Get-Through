"""
https://www.acmicpc.net/problem/1389
"""

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())

answers = [0] * (n + 1)
graphs = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

def bfs(start: int):
    global n
    q = deque([[start, 0]])
    visited = [False] * (n + 1)
    visited[start] = True
    result = 0
    while q:
        v = q.popleft()
        result += v[1]
        for i in graphs[v[0]]:
            if not visited[i]:
                q.append([i, v[1] + 1])
                visited[i] = True
    return result

for i in range(n + 1):
    answers[i] = bfs(i)

print(answers.index(min(answers[1:])))