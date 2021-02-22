"""
https://www.acmicpc.net/problem/q1027
"""


from sys import stdin

input = stdin.readline

n = int(input())
buildings = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    max_val = -1e9
    for j in range(i + 1, n):
        degree = (buildings[j] - buildings[i]) / (j - i)
        if degree > max_val:
            max_val = degree
            dp[i] += 1
            dp[j] += 1

print(max(dp))