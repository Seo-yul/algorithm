# 주사위 3개
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.  
data_list = list(map(int, input().split()))

# print(data_list)
data_set_list = list(set(data_list))
diff_count = len(data_set_list)
result = 0

# 같은눈 3개 diff_count == 1
if diff_count == 1:
    result = 10000 + int(data_set_list[0])*1000
    
# 같은눈 2개 diff_count == 2
elif diff_count == 2:
    idx = [data_list.count(data_set_list[0]), data_list.count(data_set_list[1])].index(2)
    result = data_set_list[idx]*100 + 1000

# 모두 다른 눈 diff_count == 3
else:
    result = (max(data_set_list))*100

print(result)