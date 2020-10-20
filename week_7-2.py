"""
두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.

문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
가능한 C 중에 가장 긴 문자열을 C로 한다.
위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.
이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.
"""
def gcdString(A, B):
    standard = min(len(A), len(B))
    for i in range(standard, 0, -1):
        if standard == len(A):
            t = A[:i]
            q, r = divmod(len(B), len(t))
            if t*q == B and r == 0:
                return t
        else:
            t = B[:i]
            q, r = divmod(len(A), len(t))
            if t*q == A and r == 0:
                return t
    return ''


A = 'ababcde'
B = 'ababcde'
print(f'출력: {gcdString(A, B)!r}')

A = 'ababababab'
B = 'abab'
print(f'출력: {gcdString(A, B)!r}')

A = 'abababab'
B = 'abab'
print(f'출력: {gcdString(A, B)!r}')

A = 'fast'
B = 'campus'
print(f'출력: {gcdString(A, B)!r}')