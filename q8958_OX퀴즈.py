"""
https://www.acmicpc.net/problem/q8958
"""

t = int(input())

answers = [0] * t

def score(string: str):
    answer = 0
    combo = 0
    for s in string:
        combo = combo + 1 if s == "O" else 0
        answer += combo
    return answer

for i in range(t):
    s = input()
    answers[i] = score(s)

print("\n".join(list(map(str, answers))))