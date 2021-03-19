"""
https://www.acmicpc.net/problem/1188
"""

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

def gcd(a: int, b: int):
    if a % b == 0:
        return b
    return gcd(b, a % b)

print(m - gcd(n, m))