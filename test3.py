data_ = list(map(int, input().split()))
def solution(A):
    # write your code in Python 3.6
    result_cnt = 0
    cnt = 1
    
    A.sort()
    A_len = len(A)
    max_cnt = A_len
    min_cnt = 1
    print(A)
    while A:
        if A[A_len-1] == max_cnt:
            A.pop()
            A_len -= 1
            max_cnt -= 1
        else:
            if A[A_len-1] > max_cnt:
                A[A_len-1] -= 1
            else:
                A[A_len-1] += 1
            result_cnt += 1
        
        if A:
            if A[0] == min_cnt:
                del A[0]
                min_cnt += 1
                A_len -= 1
            else:
                if A[0] > min_cnt:
                    A[0] -= 1
                if A[0] < min_cnt:
                    A[0] += 1
                result_cnt +=1
        
        if result_cnt > 1000000000:
            return -1
    return result_cnt

solution(data_)