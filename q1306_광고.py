"""
https://www.acmicpc.net/problem/1306
"""

from sys import stdin

input = stdin.readline

n = int(input())
string = input()

pi = [0] * 1000001

j = 0

for i in range(1, n):
    while (string[i] != string[j]) and j > 0:
        j = pi[j-1]
    if string[i] == string[j]:
        j += 1
        pi[i] = j

print(n - pi[n-1])