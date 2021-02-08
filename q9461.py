"""
https://www.acmicpc.net/problem/9461
"""

t = int(input())
test_cases = [int(input()) for _ in range(t)]
padovan = [1, 1, 1, 2, 2]

for case in test_cases:
    if case < 6:
        print(padovan[case-1])
        continue
    padovan_replica = list(padovan)
    for j in range(case - 5):
        answer = padovan_replica[-1] + padovan_replica[-5]
        padovan_replica.append(answer)
    print(padovan_replica[-1])