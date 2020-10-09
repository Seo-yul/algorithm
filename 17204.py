N, K = map(int, input().split())
point_list = [0]*N
for i in range(N):
    point_list[i] = int(input())


result = 1
def pinger(idx, data_list, _K, result):
    if result > N:
        result = -1
        return result

    if data_list[idx] == _K:        
        return result

    else:
        result += 1
        i = data_list[idx]        
        return pinger(i, data_list, _K, result)

result = pinger(0, point_list, K, result)

print(result)