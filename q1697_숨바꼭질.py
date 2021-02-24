"""
https://www.acmicpc.net/problem/1697
"""

from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001

def bfs():
    global n, k
    time = 0
    found = False
    q = deque([[n, 0]])
    visited[n] = True
    while q:
        v = q.popleft()
        for i in [v[0] - 1, 2 * v[0], v[0] + 1]:
            if i < 0 or i > len(visited) - 1:
                continue
            if not visited[i]:
                if i == k:
                    found = True
                    time = v[1] + 1
                q.append([i, v[1] + 1])
                visited[i] = True
        if found:
            break
    return time

print(bfs())
