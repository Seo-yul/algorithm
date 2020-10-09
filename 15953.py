"""
제1회 코드 페스티벌 본선에 진출하여 a등(1 ≤ a ≤ 100)등을 하였다. 단, 진출하지 못했다면 a = 0으로 둔다.
1등	500만원	1명
2등	300만원	2명
3등	200만원	3명
4등	50만원	4명
5등	30만원	5명
6등	10만원	6명

제2회 코드 페스티벌 본선에 진출하여 b등(1 ≤ b ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 b = 0으로 둔다.
1등	512만원	1명
2등	256만원	2명
3등	128만원	4명
4등	64만원	8명
5등	32만원	16명

첫 번째 줄에 제이지가 상상력을 발휘하여 가정한 횟수 T(1 ≤ T ≤ 1,000)가 주어진다.

다음 T개 줄에는 한 줄에 하나씩 제이지가 해본 가정에 대한 정보가 주어진다.
각 줄에는 두 개의 음이 아닌 정수 a(0 ≤ a ≤ 100)와 b(0 ≤ b ≤ 64)가 공백 하나를 사이로 두고 주어진다.

각 가정이 성립할 때 제이지가 받을 상금을 원 단위의 정수로 한 줄에 하나씩 출력한다. 입력이 들어오는 순서대로 출력해야 한다.
"""
prize_one = list()
prize_two = list()

prize_one.extend([500] * 1)
prize_one.extend([300] * 2)
prize_one.extend([200] * 3)
prize_one.extend([50] * 4)
prize_one.extend([30] * 5)
prize_one.extend([10] * 6)

prize_two.extend([512] * 1)
prize_two.extend([256] * 2)
prize_two.extend([128] * 4)
prize_two.extend([64] * 8)
prize_two.extend([32] * 16)

def code_festival(a, b, reward_one, reward_two):
    total_money = 0
    if 0< a <= len(reward_one):
        total_money = reward_one[a-1]
    
    if 0< b <= len(reward_two):
        total_money += reward_two[b-1]
    return total_money

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(code_festival(a, b, prize_one, prize_two)*10000)


