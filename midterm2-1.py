"""
철수와 친구들은 다함께 용돈을 모은 총 x원을 모두 소진하여 중국집에서 배달을 시키려고 한다.
각 음식의 가격은 food_list로 주어질 때, x원을 소진하기 위한 최소한의 음식 갯수를 반환하는 함수 solution을 완성하시오.

예시 입출력
x	food_list	return
20000	[100, 1500, 1200, 300]	16

"""
# 과제 1번 코드란

def solution(x, food_list):
    food_list.sort(reverse=True)
    cnt = 0
    for price in food_list:
        c, x = divmod(x, price)
        cnt += c
    return cnt

print(solution(20000, [100, 1500, 1200, 300]))