# 과제 8번 코드란
def solution(N, K, L, apples, moves):
    board = [[0] * (N + 1) for i in range(N + 1)]
    for x, y in apples:
        board[x][y] = 1

    oper = moves
    snake = [(1, 1)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d_f = 0
    score = 0
    x, y = 1, 1

    while True:
        score += 1
        x += d[d_f][0]
        y += d[d_f][1]
        if 1 <= x <= N and 1 <= y <= N:
            snake.append((x, y))
            for i in snake[:-1]:
                if (x, y) == i:
                    return score
            if board[x][y] == 0:
                snake.pop(0)
            if board[x][y] == 1:
                board[x][y] = 0
        else:
            return score

        if oper and score == int(oper[0][0]):
            if oper[0][1] == 'D':
                d_f = (d_f + 1) % 4
                oper.pop(0)
            elif oper[0][1] == 'L':
                d_f = (d_f - 1) % 4
                oper.pop(0)


N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
print(solution(N, K, L, apples, moves))

N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))

N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))