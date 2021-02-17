"""
https://www.acmicpc.net/problem/7567
"""

string = input()

cur_char = ""
n = 0

for char in string:
    if char != cur_char:
        n += 10
        cur_char = char
    else:
        n += 5

print(n)        
