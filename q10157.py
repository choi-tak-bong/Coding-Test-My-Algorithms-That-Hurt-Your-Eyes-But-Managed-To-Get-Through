"""
https://www.acmicpc.net/problem/10157
"""


c, r = map(int, input().split())
k = int(input())

min_value = min(c, r)
right_left = list(range(c - 1, c - min_value - 1, -1))
down_up = list(range(r, r - min_value, -1))

if len(right_left) % 2 == 1:
    right_left += [0]

if len(down_up) % 2 == 1:
    down_up += [0]

if min_value % 2 == 1:
    min_value += 1

right, left = [right_left[i] for i in range(0, min_value, 2)], [right_left[i] for i in range(1, min_value, 2)]
down, up = [down_up[i] for i in range(0, min_value, 2)], [down_up[i] for i in range(1, min_value, 2)]

united = [[down[i], right[i], up[i], left[i]] for i in range(min_value // 2)]

orders = []

for order in united:
    orders += [list([0, 1])] * order[0] + [list([1, 0])] * order[1] + [list([0, -1])] * order[2] + [list([-1, 0])] * order[3]

coord = [1, 0]
coords = []

for i in range(len(orders)):
    coord[0] += orders[i][0]
    coord[1] += orders[i][1]
    coords.append(list(coord))

print(coords[k-1][0], coords[k-1][1]) if k <= (c * r) else print(0)

