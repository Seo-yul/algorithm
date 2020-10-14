"""
Generator ABC를 구현하여 아래와 같은 동작을 하는 제네레이터 클래스를 작성하시오.
클래스의 이름은 Factorization으로 한다.
클래스 생성 시 정수 n을 입력받는다.
제네레이터는 n번 반복 가능하며, i번째 출력은 아래와 같다.
숫자 i는 1부터 시작하며, 마지막 숫자는 n이다.
숫자 i를 소인수분해한 결과를 딕셔너리로 출력한다.
딕셔너리의 key는 소인수를, value는 해당 소인수의 지수를 나타낸다.
ex) i = 18 -> 2^1 * 3^2 -> {2:1, 3:2}

"""
from collections.abc import Generator
from collections import Counter

class Factorization():
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(1, self.n+1):
            yield self.make_factorization(i)

    def getPrimaryNum_Eratos(self, n):
        nums = [True] * (n + 1)
        for i in range(2, len(nums) // 2 + 1):
            if nums[i] == True:
                for j in range(i + i, n, i):
                    nums[j] = False
        return [i for i in range(2, n) if nums[i] == True]

    def make_factorization(self, n):
        factors = []
        number = n
        prime_nums = self.getPrimaryNum_Eratos(n + 1)

        if n in prime_nums:
            factors.append(n)

        else:
            answers = []
            for prime_num in prime_nums:
                if n % prime_num == 0:
                    while (n % prime_num == 0):
                        answers.append(prime_num)
                        n = n // prime_num

            for num in answers:
                factors.append(num)
        result = dict(Counter(factors))
        if number == 1:
            return 'i = {} {}'.format(number,{1:1} )
        else:
            return 'i = {} {}'.format(number,result )

fact = Factorization(20)
for elem in fact:
    print(elem)








