"""
https://www.acmicpc.net/problem/3190
"""

from typing import List

GROUND = 0
WALL = 1
APPLE = 2
SNAKE = 3
TAIL = 4

class Snake:
    def __init__(self) -> None:
        self.x = 1
        self.y = 1
        self.d = 0
        self.dx: List[int] = [1, 0, -1, 0]
        self.dy: List[int] = [0, 1, 0, -1]
        self.tails: List[List[int]] = []
        self.movable = True

    def move(self):
        fx = self.x + self.dx[self.d]
        fy = self.y + self.dy[self.d]

        if board[fy][fx] == GROUND:
            board[self.y][self.x] = TAIL
            self.tails.append([self.x, self.y])
            board[self.tails[0][1]][self.tails[0][0]] = GROUND
            self.tails.pop(0)
            board[fy][fx] = SNAKE
            self.x, self.y = fx, fy
        elif board[fy][fx] == WALL:
            self.movable = False
        elif board[fy][fx] == TAIL:
            self.movable = False
        elif board[fy][fx] == APPLE:
            board[self.y][self.x] = TAIL
            self.tails.append([self.x, self.y])
            board[fy][fx] = SNAKE
            self.x, self.y = fx, fy

    def turn(self, direction: str):
        if direction == "D":
            self.d = self.d + 1 if self.d < 3 else 0
        elif direction == "L":
            self.d = self.d - 1 if self.d > 0 else 3

n = int(input())
k = int(input())
apples: List[List[int]] = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
orders: List[List[str]] = [list(input().split()) for _ in range(l)]
orders: List[List[int or str]] = [[int(info[0]), info[1]] for info in orders]
time = 0

board: List[List[int]] = [[WALL] * (n + 2) for _ in range(n + 2)]

for line in board[1:n+1]:
    line[1:n+1] = [GROUND] * n

for apple in apples:
    board[apple[0]][apple[1]] = APPLE

snk = Snake()

while True:
    time += 1
    snk.move()
    if not snk.movable:
        break
    for i in range(len(orders)):
        if orders[i][0] == time:
            snk.turn(orders[i][1])

print(time)