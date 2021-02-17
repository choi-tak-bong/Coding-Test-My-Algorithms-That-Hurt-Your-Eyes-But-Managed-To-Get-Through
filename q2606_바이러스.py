"""
https://www.acmicpc.net/problem/2606
"""

from collections import deque

n = int(input())
node = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

for _ in range(node):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    global answer
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                answer += 1
                visited[i] = True
bfs(1)
print(answer)