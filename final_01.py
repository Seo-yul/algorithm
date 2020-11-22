def solution(s):
    result = ''
    s_len = len(s) // 2
    w = s[:s_len]
    rw = s[-1:-s_len-1:-1]
    if w != rw:
        result = w
        result += w[-1::-1]

    return result


s = 'abcdcba'
print(solution(s))

s = 'bannana'
print(solution(s))

s = 'wabe'
print(solution(s))