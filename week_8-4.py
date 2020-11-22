"""
정수로 이루어진 수열 x가 주어졌을 때,
x[i-1] < x[i], x[i+1] < x[i]인 x[i]를 피크라고 부른다.
a에 피크가 단 하나 존재할 때, 피크를 찾아 출력하는 O(logN) 알고리즘을 구현하시오.

예시 입력

x	                                            출력
[-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]	6
[-1, -1, -1, -1, 0, 1, 20, 19, 17]	            20
"""

answer = None
cnt = 0
def sol(lst, idx, s):
    global answer, cnt
    length = len(lst)

    if answer is not None:
        return

    if idx <= 1 or idx >= length-2:
        return

    if lst[idx-1] < lst[idx] and lst[idx+1] < lst[idx]:
        answer = lst[idx]
        return

    cnt += 1
    if s == 'l' or s == 's':
        sol(lst, idx - (idx//2), 'l')
        if answer is None:
            sol(lst, idx - (idx // 2 + 1), 'l')

    if s == 'r' or s == 's':
        sol(lst, idx + (idx//2), 'r')
        if answer is None:
            sol(lst, idx + (idx // 2 - 1), 'r')








def solution(x):
    if len(x) < 3:
        return None

    i = len(x) // 2
    sol(x, i, 's')
    return answer

# data = [-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]
# print(solution(data))

data = [-1, -1, -1, -1, 0, 1, 20, 19, 17]
print(solution(data))

# data = []
# print(solution(data))
