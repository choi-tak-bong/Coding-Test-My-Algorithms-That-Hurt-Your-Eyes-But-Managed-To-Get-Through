from sys import stdin

input = stdin.readline

n = int(input())

board = [[0] * n for _ in range(n)]

def create_star(x: int, y: int, leng: int):
    sliced_leng = leng // 3

    if leng == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    board[i+x][j+y] = 1
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    create_star(x + i * sliced_leng, y + j * sliced_leng, sliced_leng)

create_star(0, 0, n)

for i in range(n):
    for j in range(n):
        print("*" if board[i][j] == 1 else " ", end="")
    print("")
