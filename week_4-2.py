"""
아래 기능을 수행하는 coroutine 함수를 구현하시오.

coroutine 생성 시 정수 n을 입력받는다.
매번 실행 시 정수 x를 입력받는다.
coroutine의 상태는 현재까지 입력받은 x값 중 가장 작은 수이다.
coroutine은 n번까지 실행 후 종료된다.
"""

def coroutine(n):
    k = n
    x = yield n
    for i in range(k):
        if x > n:
            x = n
        n = yield x
        print('yield 가 실행된다. 처음 4에서')

"""
아래 주어진 테스트 코드에서 반드시 정상 동작하도록 코드를 작성하시오.
"""
# Test code
c = coroutine(10)
next(c)
print(c.send(20))
print(c.send(5))
print(c.send(6))
print(c.send(8))
try:
    print(c.send(2))
except StopIteration:
    print('successful')