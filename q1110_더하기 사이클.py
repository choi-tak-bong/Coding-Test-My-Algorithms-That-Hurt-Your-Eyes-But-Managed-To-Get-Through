"""
https://www.acmicpc.net/problem/1110
"""

from sys import stdin

input = stdin.readline

n = int(input())
first = n
i = 0

while True:
    a = n // 10
    b = n % 10
    c = (a + b) // 10
    d = (a + b) % 10
    n = 10 * b + d
    i += 1
    if n == first:
        break
    
print(i)