"""
https://www.acmicpc.net/problem/15650
"""


from itertools import combinations

n, m = map(int, input().split())

number_list = list(range(1, n + 1))
number_combination = list(combinations(number_list, m))

for i in range(len(number_combination)):
    for j in range(len(number_combination[i])):
        print(number_combination[i][j], end=" ")
    print("")
