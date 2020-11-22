"""
n개의 정수로 이루어진 리스트 nums와 정수 target이 주어졌을 때,
nums에 있는 정수 4개를 합하여 target을 만들 수 있는 모든 조합을 구하시오.
단, 정답에는 동일한 정수 조합이 여러개 포함되어서는 안된다.

예시 입력
nums = [1, 0, -1, 0, -2, 2]
target = 0

출력:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
import itertools
def solution(nums, target):
    data_iter = itertools.combinations(nums,4)
    answer = [list(data) for data in data_iter if sum(data) == target]
    return answer


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(solution(nums, target))