from sys import stdin

input = stdin.readline

m, n = map(int, input().split())

talpi = min(m, n) // 2
m -= talpi * 2; n -= talpi * 2

if m == 0 or n == 0:
    talpi -= 1
    m += 2; n += 2

def last(m, n):
    if m == 2: return 2
    if n == 2: return 3
    if m == 1: return 0
    if n == 1: return 1
    return 0

curve_count = 4 * talpi + last(m, n)

row = 1; col = 1
row += talpi; col += talpi

if m == 2 or n == 2:
    row += 1

if m == 1:
    col += n - 1

if n == 1:
    row += m - 1

print(curve_count)
print(row, col)