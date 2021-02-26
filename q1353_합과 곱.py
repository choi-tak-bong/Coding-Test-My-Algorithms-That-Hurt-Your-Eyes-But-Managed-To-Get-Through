"""
https://www.acmicpc.net/problem/1353
"""

from sys import stdin

input = stdin.readline

s, p = map(int, input().split())

i = 2

prev_v = 0
cur_v = 0

while True:
    cur_v = (s / i) ** i
    if s == p:
        i = 1
        break
    if cur_v >= p:
        break
    elif cur_v < prev_v:
        i = -1
        break
    prev_v = cur_v
    i += 1

print(i)