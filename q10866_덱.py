"""
https://www.acmicpc.net/problem/10866
"""

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
answer = []
answer_append = answer.append

q = deque([])

for _ in range(n):
    s = input().split()
    order = s[0]
    if order == "push_front":
        q.appendleft(s[1])
    elif order == "push_back":
        q.append(s[1])
    elif order == "pop_front":
        answer_append(q.popleft() if len(q) > 0 else "-1")
    elif order == "pop_back":
        answer_append(q.pop() if len(q) > 0 else "-1")
    elif order == "size":
        answer_append(str(len(q)))
    elif order == "empty":
        answer_append("1" if len(q) == 0 else "0")
    elif order == "front":
        answer_append(q[0] if len(q) > 0 else "-1")
    elif order == "back":
        answer_append(q[-1] if len(q) > 0 else "-1")

print("\n".join(answer))