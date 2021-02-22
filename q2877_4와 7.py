"""
https://www.acmicpc.net/problem/q2877
"""

from sys import stdin

input = stdin.readline

n = int(input())

i = 2
j = 1
a, b = 0, 2

while True:
    if a <= n <= b:
        break
    else:
        i *= 2
        j += 1
        a = b
        b = b + i

answer = ""

b, n, a = b - a, n - a, 1

def create_answer(start: int, end: int, repeat: int):
    global answer, n
    mid = (end + start) / 2
    if repeat == 0:
        return
    if mid > n:
        answer += "4"
        create_answer(start, mid, repeat-1)
    elif mid < n:
        answer += "7"
        create_answer(mid, end, repeat-1)

create_answer(a, b, j)
print(answer)