"""
https://www.acmicpc.net/problem/q1082
"""

from sys import stdin

input = stdin.readline

n = int(input())
prices = list(map(int, input().split()))
m = int(input())

min_value = min(prices)
min_index = n - 1

for i in range(len(prices) - 1, -1, -1):
    if prices[min_index] > prices[i]:
        min_index = i

cur_m = m - (min_value * (m // min_value))
dp = [min_index] * (m // min_value)

start_pointer = 0
pointer_move = True

for i in range(len(dp)):
    cur_m += min_value # 기존에 배치된 번호를 되팔아서 기존에 배치된 번호의 가격 만큼 확보한다.

    for j in range(n - 1, -1, -1):
        if prices[j] <= cur_m and j > 0: # 번호를 살 수 있는 경우, 가격이 번호 0의 가격보다 비싼 경우
            cur_m -= prices[j]
            dp[i] = j
            pointer_move = False
            break
        elif prices[j] <= cur_m and j == 0 and pointer_move: # 번호를 살 수 있는 경우, 가격이 0만 살 수 있는 경우, 포인터 이동이 True인 경우
            start_pointer += 1
        elif prices[j] <= cur_m and j == 0 and not pointer_move: # 번호를 살 수 있는 경우, 가격이 0만 살 수 있는 경우, 포인터 이동이 False인 경우
            cur_m -= prices[j]

print("".join(map(str, dp[start_pointer:])) if start_pointer < len(dp) else 0)