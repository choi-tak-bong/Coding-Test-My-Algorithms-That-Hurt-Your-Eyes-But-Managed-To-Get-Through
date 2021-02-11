"""
https://www.acmicpc.net/problem/2583
"""

import sys

sys.setrecursionlimit(100000) # 재귀함수 한계 설정

m, n, k = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(k)]
board = [[0] * n for _ in range(m)]
visited = [False] * (m * n)
space_num = 0
island_sizes = [0] * 5000

def check_islands(index, x, y):
    global m, n
    # 영역을 넘어가면 종료
    if x < 0 or y < 0 or x > len(board[0]) - 1 or y > len(board) - 1:
        return
    
    # 막힌 곳이면 종료
    if board[y][x] == 1:
        return
    
    # 방문한 곳이면 종료
    if visited[y*n+x]:
        return
    
    # 해당 위치를 방문했다고 표시
    visited[y*n+x] = True

    # 사이즈 증가
    island_sizes[index] += 1

    # 상하좌우 재귀함수 실행
    check_islands(index, x, y - 1)
    check_islands(index, x, y + 1)
    check_islands(index, x - 1, y)
    check_islands(index, x + 1, y)

for square in squares:
    for i in range(square[1], square[3]):
        for j in range(square[0], square[2]):
            board[i][j] = 1

for i in range(len(board)):
    for j in range(len(board[i])):
        if visited[i*n+j] == False and board[i][j] == 0:
            check_islands(space_num, j, i)
            space_num += 1

island_sizes.sort()

print(space_num)
for i in range(len(island_sizes)):
    if island_sizes[i] != 0:
        print(island_sizes[i], end=" ")