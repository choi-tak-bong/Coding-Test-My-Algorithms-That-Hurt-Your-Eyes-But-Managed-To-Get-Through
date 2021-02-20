"""

"""

from sys import stdin

input = stdin.readline

n = int(input())
cranes_limit = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box_weight = sorted(list(map(int, input().split())), reverse=True)

sec = 0
checked = [0 for _ in range(m)]
cnt = 0

positions = [0] * n

if max(box_weight) > max(cranes_limit):
    print(-1)
else:
    while cnt < len(box_weight):
        for i in range(n):
            while positions[i] < len(box_weight):
                if not checked[positions[i]] and cranes_limit[i] >= box_weight[positions[i]]:
                    checked[positions[i]] = True
                    positions[i] += 1
                    cnt += 1
                    break
                positions[i] += 1
        sec += 1
    print(sec)