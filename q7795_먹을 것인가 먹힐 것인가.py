"""
https://www.acmicpc.net/problem/7795
"""

from sys import stdin

input = stdin.readline

t = int(input())
answers = [0] * t

for i in range(t):
    a_size, b_size = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    a_pointer, b_pointer = 0, 0
    result = 0
    
    while True:
        if a_pointer == a_size or b_pointer == b_size:
            break

        if a[a_pointer] > b[b_pointer]:
            result += b_size - b_pointer
            a_pointer += 1
        else:
            b_pointer += 1

    answers[i] = result

print("\n".join(map(str, answers)))
