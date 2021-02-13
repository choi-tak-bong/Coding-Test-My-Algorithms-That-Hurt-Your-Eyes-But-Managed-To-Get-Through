"""
https://www.acmicpc.net/problem/1253
"""

n = input()
a = list(map(int, input().split()))
a.sort()

answer = 0

number_pointer = 0
start_pointer = 0
end_pointer = len(a) - 1

while True:
    # 넘버 포인터가 초과할 경우 루프 종료
    if number_pointer == len(a):
        break

    # 시작 포인터 또는 끝 포인터 조정
    if number_pointer == start_pointer:
        start_pointer += 1
    elif number_pointer == end_pointer:
        end_pointer -= 1

    # 시작 포인터와, 끝 포인터가 만났을 경우, 포인터 초기화
    if start_pointer == end_pointer:
        number_pointer += 1
        start_pointer = 0
        end_pointer = len(a) - 1
        continue

    temp = a[start_pointer] + a[end_pointer]

    if temp > a[number_pointer]:
        end_pointer -= 1
    elif temp < a[number_pointer]:
        start_pointer += 1
    elif temp == a[number_pointer]: # 좋은 수인 경우가 있을 경우 
        answer += 1 # 정답 수 증가
        number_pointer += 1 # 넘버 포인터 증가
        start_pointer = 0 # 시작 포인터, 끝 포인터 초기화
        end_pointer = len(a) - 1

print(answer)