"""
https://www.acmicpc.net/problem/18405
"""
from collections import deque
from typing import List

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = []

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            q.append(list([board[i][j], j, i]))

q.sort(key=lambda x: x[0])
q = deque(q)

def spread_virus(virus_info: List[int]):
    global n
    v_type, vx, vy = virus_info
    for i in range(4):
        if vx + dx[i] < 0 or vy + dy[i] < 0 or vx + dx[i] > n - 1 or vy + dy[i] > n - 1:
            continue
        if board[vy+dy[i]][vx+dx[i]] != 0:
            continue
        board[vy+dy[i]][vx+dx[i]] = v_type
        q.append([v_type, vx+dx[i], vy+dy[i]])

for i in range(s):
    for _ in range(len(q)):
        v = q.popleft()
        spread_virus(v)

print(board[x-1][y-1])
