import itertools

# def permute(arr):
#     result = [arr[:]]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr):
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             result.append(arr[:])
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return result


def solution(n, k):
    return list(list(itertools.permutations([i+1 for i in range(n)], n))[k-1])

print(solution(3, 3))
print(solution(4, 9))

# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
#
# t = itertools.permutations(pool, 3)
# print(list(t))
#
# c = itertools.combinations(pool, 3)
# print(list(c))