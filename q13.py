"""
https://www.acmicpc.net/problem/15686
"""

from typing import List, Tuple
from itertools import combinations

NULL = 0
HOUSE = 1
CHICKEN = 2

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

chickens: List[Tuple[int, int]] = []
houses: List[Tuple[int, int]] = []

for i in range(len(city)): # max_compl = 50*50 = 2500
    for j in range(len(city[i])):
        if city[i][j] == HOUSE:
            houses.append((j, i))
        elif city[i][j] == CHICKEN:
            chickens.append((j, i))

chicken_selected: List[List[Tuple[int, int]]] = tuple(combinations(chickens, m))

def calc_chicken_length(chick_list: List[Tuple[int, int]], house_list: List[Tuple[int, int]]):
    answer = 0
    for house in house_list:
        min_value = 1e9
        for chick in chick_list:
            chick_len = abs(house[0] - chick[0]) + abs(house[1] - chick[1])
            min_value = min(min_value, chick_len)
        answer += min_value
    return answer

min_value = 1e9
for selected_one in chicken_selected:
    min_value = min(min_value, calc_chicken_length(selected_one, houses))

print(min_value)