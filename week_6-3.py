'''
N개의 문자열로 이루어진 List에서 전체 문자열이 앞 n개 문자열이 같다고 할때, 가장 큰 n을 출력하는 알고리즘을 구현하라.
'''


def solution(a):
    answer = 0
    standard = a[0]
    for i in range(len(standard)):
        f = True
        for word in range(1, len(a)):
            if standard[i] != a[word][i]:
                f = False
            if not f:
                break
        if not f:
            break
        answer += 1
    return answer


print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg']))  # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg']))  # 0