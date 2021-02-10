"""
https://www.acmicpc.net/problem/12865
"""

n, k = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(n)]

def knapsack(capacity, n):
    array = [[0 for _ in range(capacity + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        for s in range(1, capacity + 1):
            if stuffs[i-1][0] > s:
                array[i][s] = array[i-1][s]
            else:
                array[i][s] = max(stuffs[i-1][1] + array[i-1][s-stuffs[i-1][0]], array[i-1][s])
    return array[n][capacity]

print(knapsack(k, n))

"""
8 8
5 14
3 10
8 0
8 12
4 1
3 13
1 12
2 0
"""