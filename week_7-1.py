"""
이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다.
인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서 target을 찾으면 True를 반환하고,
target을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.
"""


def searchMatrix(matrix, target):
    print('target =', target)

    def bigSearch(mtrix):
        m = len(mtrix) // 2
        if target < mtrix[m][0]:
            return bigSearch(mtrix[:m])
        elif target > mtrix[m][len(mtrix[m])-1]:
            return bigSearch(mtrix[m+1:])
        else:
            return mtrix[m]

    mm = bigSearch(matrix)
    if target in mm:
        return True
    return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print(f'출력: {searchMatrix(matrix, 3)} ')
print(f'출력: {searchMatrix(matrix, 13)} ')