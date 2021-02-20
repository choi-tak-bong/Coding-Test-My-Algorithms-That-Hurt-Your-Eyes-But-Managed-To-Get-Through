"""
https://www.acmicpc.net/problem/2502
"""

import sys

input = sys.stdin.readline

d, k = map(int, input().split())

dp_a = [1, 0, 1, 1] + [0] * 30
dp_b = [0, 1, 1, 2] + [0] * 30

for i in range(4, 34):
    dp_a[i] = dp_a[i-1] + dp_a[i-2]
    dp_b[i] = dp_b[i-1] + dp_b[i-2]

a = 1
b = 1

d -= 1

for i in range(1, (k - dp_a[d] - dp_b[d]) // dp_a[d]):
    if (k - dp_a[d] * i) % dp_b[d] == 0 and i < (k - dp_a[d] * i) // dp_b[d]:
        a = i
        b = (k - dp_a[d] * i) // dp_b[d]

print(a)
print(b)
