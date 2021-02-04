from typing import List

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
tri_copy = [list(tri[i]) for i in range(n)]

for i in range(len(tri) - 1):
    for j in range(len(tri[i])):
        tri_copy[i+1][j] = max(tri_copy[i+1][j], tri_copy[i][j] + tri[i+1][j])
        tri_copy[i+1][j+1] = max(tri_copy[i+1][j+1], tri_copy[i][j] + tri[i+1][j+1])

print(max(tri_copy[-1]))
