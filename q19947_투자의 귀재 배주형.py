"""
https://www.acmicpc.net/problem/19947
"""

from sys import stdin

MAX = 11

input = stdin.readline

h, y = map(int, input().split())
dp = [h] * MAX
invest_years = [1, 3, 5]
invest_ratios = [1.05, 1.2, 1.35]

for i in range(3):
    dp[invest_years[i]] = max(dp[invest_years[i]], int(h * invest_ratios[i]))

    for j in range(invest_years[i] + 1, MAX):
        dp[j] = max(dp[j], int(dp[j-invest_years[i]] * invest_ratios[i]))

print(dp[y])