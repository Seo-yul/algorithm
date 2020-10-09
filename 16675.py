# 첫 번째 줄에 차례로 ML, MR, TL, TR이 공백으로 구분되어 주어진다. 차례대로 민성이의 왼손과 오른손, 태경이의 왼손과 오른손의 상태를 나타낸다.
# 위 4개의 값들은 “S”, “R”, “P” 중 하나이며, 각각 가위, 바위, 보를 의미한다.

# 첫 번째 줄에 민성이가 무조건 이길 수 있다면 “MS”, 태경이가 무조건 이길 수 있다면 “TK”, 누가 이길 지 확답할 수 없다면 “?”를 쌍따옴표를 제외하고 출력한다.
# 가위바위보에서 가위는 보를 이기고, 바위는 가위를 이기며, 보는 바위를 이긴다. 같은 손동작끼리는 승부가 나지 않는다 (비긴다).
ML, MR, TL, TR = input().split(' ')

ms_hands = [ML, MR]
tk_hands = [TL, TR]

ms_score = [0, 0]
tk_score = [0, 0]
for i in range(len(ms_hands)):
    for j in range(len(tk_hands)):
        if ms_hands[i] == 'R' and tk_hands[j] == 'S':
            ms_score[i] += 1

        elif ms_hands[i] == 'R' and tk_hands[j] == 'P':
            tk_score[j] += 1

        if ms_hands[i] == 'S' and tk_hands[j] == 'P':
            ms_score[i] += 1

        elif ms_hands[i] == 'S' and tk_hands[j] == 'R':

            tk_score[j] += 1

        if ms_hands[i] == 'P' and tk_hands[j] == 'R':
            ms_score[i] += 1

        elif ms_hands[i] == 'P' and tk_hands[j] == 'S':

            tk_score[j] += 1

if 2 in ms_score:
    print('MS')
elif 2 in tk_score:
    print('TK')
else:
    print('?')

