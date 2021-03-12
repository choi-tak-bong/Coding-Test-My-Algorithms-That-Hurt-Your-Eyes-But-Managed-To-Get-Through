"""
https://www.acmicpc.net/problem/1004
"""

from sys import stdin

input = stdin.readline

t = int(input())
answers = [0] * t

for tc in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    
    count = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d = (cx - x1) ** 2 + (cy - y1) ** 2
        in1 = False if d > r ** 2 else True
        d = (cx - x2) ** 2 + (cy - y2) ** 2
        in2 = False if d > r ** 2 else True
        
        if in1 != in2:
            count += 1
    
    answers[tc] = count

print("\n".join(map(str, answers)))