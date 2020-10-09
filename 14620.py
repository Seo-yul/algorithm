N = int(input())
M = [list(map(int,input().split())) for i in range(N)]
dx, dy = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0] # 정지, 상, 우, 하, 좌

buy_M = [[0]*N for i in range(N)]
result = 9999 # 돈


def buy(lst):
    money = 0
    flower_list  = []
    for flower in lst:
        x = flower // N # 행 
        y = flower % N # 열 
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 9999
        
        for d in range(5):
            flower_list.append((x + dx[d], y+dy[d]))
            money += M[x + dx[d]][y+dy[d]]

    if len(set(flower_list)) != 15: # 칸이 15개가 아니면 겹쳤다는 뜻
        return 9999
    
    return money

# 씨앗 세번 뿌려
for i in range(N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            result = min(result, buy([i, j, k]))

print(result)