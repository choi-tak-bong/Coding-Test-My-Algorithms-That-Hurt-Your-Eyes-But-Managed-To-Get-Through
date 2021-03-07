"""
https://www.acmicpc.net/problem/1025
"""

from sys import stdin
from math import sqrt

input = stdin.readline

m, n = map(int, input().split())

top = []

result = -1

for _ in range(m):
    string = list(map(int, list(input().replace("\n", ""))))
    top.append(string)

for start_m in range(m):
    for start_n in range(n):
        for step_m in range(-m, m):
            for step_n in range(-n, n):
                if step_m == 0 and step_n == 0:
                    continue

                step = 0
                x = start_m
                y = start_n
                val = ""

                while (0 <= x < m) and (0 <= y < n):
                    val += str(top[x][y])
                    step += 1

                    v_int = int("".join(val))
                    v_sqrt = sqrt(v_int)
                    v_decimal = v_sqrt - int(v_sqrt)

                    if v_decimal == 0 and v_int > result:
                        result = v_int

                    x = start_m + step * step_m
                    y = start_n + step * step_n

print(result)
