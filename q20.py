"""
https://www.acmicpc.net/problem/18428
"""

from typing import List, Tuple
from itertools import combinations

WALL = "w"

n = int(input())
board: List[List[str]] = [list(input().lower().split()) for _ in range(n)]
avail_coords: List[Tuple[int, int]] = []
teacher_coords: List[Tuple[int, int]] = []

for i in range(n):
    for j in range(n):
        if board[i][j] == "x":
            avail_coords.append((j, i))
        elif board[i][j] == "t":
            teacher_coords.append((j, i))

avail_coords_combis: List[Tuple[Tuple[int, int]]] = list(combinations(avail_coords, 3))

def check_coords_range(obstacle_coords: Tuple[Tuple[int, int]]):
    global n, board, teacher_coords

    detected = False
    temp_board: List[List[str]] = [[WALL] * (n + 2) for _ in range(n + 2)]
    
    for i in range(1, n + 1):
        temp_board[i][1:n+1] = list(board[i-1])

    dx: List[int] = [0, 1, 0, -1]
    dy: List[int] = [-1, 0, 1, 0]

    # 장애물 배치
    for i in range(len(obstacle_coords)):
        temp_board[obstacle_coords[i][1]+1][obstacle_coords[i][0]+1] = "o"

    for teacher in teacher_coords:
        for direction in range(4):
            sx, sy = teacher[0] + 1, teacher[1] + 1 
            while True:
                sx = sx + dx[direction]
                sy = sy + dy[direction]
                if temp_board[sy][sx] == WALL:
                    break
                elif temp_board[sy][sx] == "o":
                    break
                elif temp_board[sy][sx] == "s":
                    detected = True
                    break

    return detected

is_any_way_not_detected = False

for combi in avail_coords_combis:
    if not check_coords_range(combi):
        is_any_way_not_detected = True

if is_any_way_not_detected:
    print("YES")
else:
    print("NO")