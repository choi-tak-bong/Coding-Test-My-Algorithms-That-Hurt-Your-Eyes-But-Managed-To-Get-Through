"""
https://www.acmicpc.net/problem/1010
"""

from typing import List
import sys

t = int(input())

input = sys.stdin.readline

orders = [list(map(int, input().split())) for _ in range(t)]

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

def get_bridge(sites_info: List[int]):
    west, east = sites_info
    upper = factorial(east)
    lower = factorial(east - west) * factorial(west)
    return int(upper / lower)

for order in orders:
    print(get_bridge(order))
