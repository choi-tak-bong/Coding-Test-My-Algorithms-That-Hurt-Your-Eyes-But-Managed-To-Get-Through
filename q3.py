"""
https://www.acmicpc.net/problem/1439
"""

from bisect import bisect_left, bisect_right

string = input()

zero_split = string.split("0")
one_split = string.split("1")

zero_split.sort()
one_split.sort()

zero_split_num = len(zero_split) - (bisect_right(zero_split, "") - bisect_left(zero_split, ""))
one_split_num = len(one_split) - (bisect_right(one_split, "") - bisect_left(one_split, ""))

answer = min(zero_split_num, one_split_num)
print(answer)
