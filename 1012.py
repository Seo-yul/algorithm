import sys
sys.setrecursionlimit(10**8)


T = int(input())
G, G_map = [], []

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    global G, G_map
    if G_map[x][y]:
        return

    G_map[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if G[xx][yy] == 0 or G_map[xx][yy] == 1:
            continue
        dfs(xx, yy)

def case_T():
    global G, G_map
    # N 행의 수 M 열의 수 K 꽃의 수
    M, N, K = map(int, input().split())
    G = [[0 for _ in range(M+2)] for i in range(N+2)]      # 맵
    G_map = [[0 for _ in range(M+2)] for i in range(N+2)]  # 탐색 확인

    for _ in range(K):
        Y, X = map(int, input().split())
        G[X+1][Y+1] = 1     # 문제에서 준 배추 위치
    result = 0 

    for i in range(1, N+1):
        for j in range(1, M+1):
            if G_map[i][j] or G[i][j] == 0: # 체크를 했거나 배추가 없으면 패스
                continue
            dfs(i, j)
            result += 1

    print(result)


for _ in range(T):
    case_T()