R, C = map(int, input().split())
house = [list(input()) for i in range(R)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

flag = False

for x in range(R):
    for y in range(C):
            if house[x][y] == 'W':
                for d in range(4): # 위 오른쪽 아래 왼쪽 확인
                    xx, yy = x + dx[d], y + dy[d]
                    if xx < 0 or xx == R or yy < 0 or yy == C:
                        continue
                    if house[xx][yy] == 'S': # 울타리 칠 공간도 없이 붙어있음
                        flag = True

if flag:
    print(0)
else:
    print(1)
    for x in range(R):
        for y in range(C):
            if house[x][y] not in 'SW': # 양이나 늑대가 있는 공간이 아님
                house[x][y] = 'D' # 다 울타리 쳐버려
    for i in house:
        print(''.join(i))
