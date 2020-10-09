"""
1에서부터 6까지의 눈을 가진 4개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 

예를 들어, 4개의 눈이 3, 3, 3, 3으로 주어지면 50,000+3*5,000으로 계산되어 65,000원의 상금을 받게 된다. 4개의 눈이 3, 3, 6, 3으로 주어지면 상금은 10,000+3*1,000으로 계산되어 13,000원을 받게 된다.
또 4개의 눈이 2, 2, 6, 6으로 주어지면 2,000+2*500+6*500으로 계산되어 6,000원을 받게 된다. 4개의 눈이 6, 2, 1, 6으로 주어지면 1,000+6*100으로 계산되어 1,600원을 받게 된다. 4개의 눈이 6, 2, 1, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금으로 받게 된다.

N(1≤N≤1,000)명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을 작성하시오.
"""
def dice_game(M):
    dice_list = sorted(M)
    dice_set_list = list(set(dice_list))
    len_dice_set = len(dice_set_list)
    if len_dice_set == 1:
        # 같은 눈이 4개가 나오면 50,000원+(같은 눈)*5,000원의 상금을 받게 된다.
        return 50000 + dice_set_list[0] * 5000
    
    elif len_dice_set == 2:
        if dice_list[1] == dice_list[2]:
            # 같은 눈이 3개만 나오면 10,000원+(3개가 나온 눈)*1,000원의 상금을 받게 된다. 
            return 10000 + dice_list[1] * 1000
        else:
            # 같은 눈이 2개씩 두 쌍이 나오는 경우에는 2,000원+(2개가 나온 눈)*500원+(또 다른 2개가 나온 눈)*500원의 상금을 받게 된다.
            return 2000 + (dice_list[1] + dice_list[2]) * 500

    elif len_dice_set == 3:
        # 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
        for i in range(3):
            if dice_list[i] == dice_list[i+1]:
                return 1000 + dice_set_list[i] * 100
            

    else:
        # 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
        return 1000 + max(dice_list) * 100

N = int(input())
money = list()
for i in range(N):
    M = list(map(int, input().split()))
    money.append(dice_game(M))
print(max(money))
