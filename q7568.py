"""
https://www.acmicpc.net/problem/7568
"""

n = int(input())
men = [tuple(map(int, input().split())) for _ in range(n)]
ranking = [1] * n

for i in range(len(men)):
    for j in range(len(men)):
        if men[i][0] < men[j][0] and men[i][1] < men[j][1]:
            ranking[i] += 1

for number in ranking:
    print(number, end=" ")