"""
https://www.acmicpc.net/problem/10845
"""

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque([])
answers = []

answers_append = answers.append

for _ in range(n):
    order = input().split()
    if order[0] == "push":
        q.append(order[1])
    elif order[0] == "pop":
        if len(q) == 0:
            answers_append("-1")
        else:
            v = q.popleft()
            answers_append(v)
    elif order[0] == "size":
        answers_append(str(len(q)))
    elif order[0] == "empty":
        if len(q) == 0:
            answers_append("1")
        else:
            answers_append("0")
    elif order[0] == "front":
        if len(q) == 0:
            answers_append("-1")
        else:
            answers_append(q[0])
    elif order[0] == "back":
        if len(q) == 0:
            answers_append("-1")
        else:
            answers_append(q[-1])

print("\n".join(answers))