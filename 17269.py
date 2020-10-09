list_alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

N, M = map(int, input().split(' '))
A, B = input().split()
name_mixed = ''
min_len = min(N, M)
for i in range(min_len):
    name_mixed += A[i] + B[i]

name_mixed += A[min_len:] + B[min_len:]

lst = [list_alpha[ord(i)-ord('A')] for i in name_mixed]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print('{}%'.format(lst[0] % 10 * 10 + lst[1] % 10))