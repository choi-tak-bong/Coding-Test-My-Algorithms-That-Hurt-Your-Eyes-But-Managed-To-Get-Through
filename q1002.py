"""
https://www.acmicpc.net/problem/1002
"""


import math as mt

n = int(input())
test_cases = [list(map(int, input().split())) for _ in range(n)]

for test_case in test_cases:
    x1, y1, r1, x2, y2, r2 = test_case
    turret_range = mt.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # 두 점에서 만나는 경우
    if abs(r2 - r1) < turret_range < r2 + r1:
        print(2)
        continue

    # 외접
    if r1 + r2 == turret_range:
        print(1)
        continue

    # 내접
    if abs(r2 - r1) == turret_range and turret_range != 0:
        print(1)
        continue

    # 원의 반지름 합이 거리보다 긴 경우
    if r2 + r1 < turret_range:
        print(0)
        continue

    # 내부에서 서로 만나지 않음
    if abs(r2 - r1) > turret_range:
        print(0)
        continue

    # 동심원
    if turret_range == 0 and r1 != r2:
        print(0)
        continue

    # 무한대
    if turret_range == 0 and r1 == r2:
        print(-1)
        continue
