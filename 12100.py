N = int(input())
M =[list(map(int, input().split())) for _ in range(N)]






def check_init():
    return [[0 for _ in range(N)] for i in range(N)]

check = check_init()
result = 0

def m_max(m):
    lst = (max(i) for i in m)
    return max(lst)

def move(k, m):
    global N
    
    

    def up(k, m):
        for i in range(1, N):
            for j in range(N):
                if m[i-1][j] == m[i][j]:
                    m[i-1][j] += m[i][j]
                    m[i][j] = 0
        return max(m_max(m), move(k-1, m))

    def down(k, m):
        for i in range(N-1,-1,-1):
            for j in range(N):
                if m[i][j] == m[i-1][j]:
                    m[i][j] += m[i-1][j]
                    m[i+1][j] = 0
        return max(m, move(k-1, m))

    def right(k):
        for i in range(N-1,-1,-1):
            for j in range(N):
                if m[j][i] == m[j][i-1]:
                    m[j][i] += m[j][i-1]
                    m[j][i+1] = 0
        return max(m, move(k-1, m))

    def left(k):
        for i in range(1, N):
            for j in range(N):
                if m[j][i-1] == m[j][i]:
                    m[j][i-1] += m[j][i]
                    m[j][i] = 0
        return max(m_max(m), move(k-1, m))
    

    if k == 0:
        return m_max(m)

    return( max( up(), down(), right(), left() ))







