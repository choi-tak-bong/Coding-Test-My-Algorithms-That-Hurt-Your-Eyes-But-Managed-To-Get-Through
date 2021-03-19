"""
https://www.acmicpc.net/problem/1461
"""

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))
minus_sides, plus_sides = [], []

result = 0

for i in range(n):
    if books[i] >= 0: plus_sides.append(-books[i])
    else: minus_sides.append(books[i])
    
minus_sides.sort(); plus_sides.sort()

for i in range(0, len(minus_sides), m):
    v = -minus_sides[i]
    result += 2 * v

for i in range(0, len(plus_sides), m):
    v = -plus_sides[i]
    result += 2 * v

if not minus_sides: result -= -plus_sides[0]
elif not plus_sides: result -= -minus_sides[0]
elif minus_sides[0] < plus_sides[0]: result -= -minus_sides[0]
else: result -= -plus_sides[0]

print(result)
