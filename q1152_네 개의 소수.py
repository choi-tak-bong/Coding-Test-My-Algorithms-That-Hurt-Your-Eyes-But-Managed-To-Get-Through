"""
https://www.acmicpc.net/problem/1152
"""

from sys import stdin
from math import sqrt

input = stdin.readline

n = int(input())

if n < 8:
    print(-1)
else:
    if n % 2:
        print("2 3 ", end="")
        n -= 5
    else:
        print("2 2 ", end="")
        n -= 4
    
    era = [True for _ in range(n + 1)] # 에라토스테네스의 채

    for i in range(2, int(sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if era[i] == True: # i가 소수인 경우(남은 수인 경우)
            j = 2
            while i * j <= n:
                era[i*j] = False
                j += 1

    for i in range(2, n+1):
        if era[i] and era[n-i]:
            print(i, n - i)
            exit()