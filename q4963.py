
boards = []

directions = [
    (0, 1), # 아래
    (1, 1), # 우측 하향
    (1, 0), # 오른쪽
    (1, -1), # 우측 상향
    (0, -1), # 위
    (-1, -1), # 좌측 상향
    (-1, 0), # 왼쪽
    (-1, 1) # 좌측 하향
]

def create_graph(board, x, y, visited, node_board):
    w, h = len(board[0]), len(board)

    # 범위를 넘어서면 종료
    if x < 0 or y < 0 or x > w - 1 or y > h - 1:
        return
    
    # 해당 지역이 바다일 경우 종료
    if board[y][x] == 0:
        return

    # 탐색한 지역일 경우 종료
    if visited[node_board[y][x]]:
        return

    # 해당 지역 탐색 완료
    visited[node_board[y][x]] = True

    # 다른 지역 탐색
    for direction in directions:
        create_graph(board, x + direction[0], y + direction[1], visited, node_board)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    boards.append(list(board))

for b in boards:
    islands = 0
    w, h = len(b[0]), len(b)
    visited = [False] * (w * h)
    node_board = [list([(w * j + i) for i in range(w)]) for j in range(h)]
    for i in range(h):
        for j in range(w):
            if b[i][j] == 1 and visited[node_board[i][j]] == False:
                islands += 1
                create_graph(b, j, i, visited, node_board)
    print(islands)
