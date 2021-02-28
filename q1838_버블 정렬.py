"""
https://www.acmicpc.net/problem/1838
"""

from sys import stdin

input = stdin.readline

idx = -1

def check_index(text: str):
    global idx
    number = int(text)
    idx += 1
    return [number, idx]

n = int(input())
numbers = sorted(list(map(check_index, input().split())))

max_index_moving = 0

for i in range(len(numbers)):
    if (numbers[i][1] - i) > max_index_moving:
        max_index_moving = numbers[i][1] - i

print(max_index_moving)

