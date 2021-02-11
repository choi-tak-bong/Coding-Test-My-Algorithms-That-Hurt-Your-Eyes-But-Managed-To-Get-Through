"""
https://www.acmicpc.net/problem/14725
"""

n = int(input())
info_array = [list(input()[2:].split()) for _ in range(n)]
true_info = []

for info in info_array:
    for i in range(len(info)):
        if info[0:i+1] not in true_info:
            true_info.append(info[0:i+1])

true_info.sort()

for info in true_info:
    floor_str = ""
    for i in range(len(info) - 1):
        floor_str += "--"
    print(floor_str + info[-1])
