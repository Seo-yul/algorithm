import itertools
def solution(a):
    answer = []
    data = itertools.permutations(a, 3)
    for iter in data:
        if sum(iter) == 0:
            answer.append(list(iter))
    return answer

print(solution([4, -2, 8, 4, -6, 12]))
print(solution([-25, -10, -7, -3, 2, 4, 8, 10]))