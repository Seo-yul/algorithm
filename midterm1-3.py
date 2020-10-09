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
import math


class Factorization(Generator):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield self.make_factorization(i)
        return

    def __repr__(self):
        return 'r'

    def get_primes(self, n):
        is_primes = [True] * n
        max_length = math.ceil(math.sqrt(n))

        for i in range(2, max_length):
            if is_primes[i]:
                for j in range(i + i, n, i):
                    is_primes[j] = False
        return [i for i in range(2, n) if is_primes[i]]

    def make_factorization(self,n):
        factors = []
        for prime in self.get_primes(n):
            count = 0
            while n % prime == 0:
                n /= prime
                count += 1
            if count > 0:
                factors.append({prime:count})
        return factors

fact = Factorization(20)
for elem in fact:
    print(elem)