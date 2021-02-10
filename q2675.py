"""
https://www.acmicpc.net/problem/2675
"""

t = int(input())
answers = []

def repeat_string(n: int, string: str):
    answer = ""
    for char in string:
        for _ in range(n):
            answer += char
    return answer

for i in range(t):
    params = list(input().split())
    params[0] = int(params[0])
    answers.append(repeat_string(params[0], params[1]))

for answer in answers:
    print(answer)