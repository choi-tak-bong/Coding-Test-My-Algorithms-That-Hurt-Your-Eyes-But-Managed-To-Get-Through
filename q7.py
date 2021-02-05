"""
https://www.acmicpc.net/problem/18406
"""

n = list(map(int, list(input())))

half_length = len(n) // 2

if sum(n[:half_length]) == sum(n[half_length:]):
    print("LUCKY")
else:
    print("READY")
