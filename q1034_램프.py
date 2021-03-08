from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
lamps = [input() for _ in range(n)]
k = int(input())

answer = -1

for i in range(n):
    off_lamp = 0
    
    for j in range(m):
        if lamps[i][j] == "0":
            off_lamp += 1
    
    hap = 0

    if off_lamp <= k and off_lamp % 2 == k % 2:
        for y in range(n):
            if lamps[i] == lamps[y]:
                hap += 1
    
    answer = max(answer, hap)

print(answer)