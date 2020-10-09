"""
아래와 같은 기능을 하는 데코레이터 함수를 구현하시오. 함수를 구현하는 데에 필요한 모듈을 import하는 코드를 답안에 반드시 포함하시오.

데코레이터 함수의 이름은 coroutine으로 한다.
primer의 데코레이터로 사용되며, 아래 기능을 수행한다.
primer로부터 coroutine을 반환한다.
coroutine의 첫 yield문까지 실행시켜, 곧바로 send가 가능하게 한다.
첫 yield문까지 실행하는 과정에서 시간이 1초 이상 소요될 경우, TimeOutError 예외를 발생시킨다.
아래 주어진 테스트 코드에서 반드시 정상 동작하도록 코드를 작성하시오.
"""

# Test code
from functools import wraps
import time

def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def delayed_coroutine(n):
    st = time.perf_counter()
    time.sleep(n)
    et = time.perf_counter()
    calc_time = (et - st)*100/100
    if calc_time >= 1:
            raise TimeoutError
    n = yield
    while True:
        n = yield n
        
 
c = delayed_coroutine(0.5)
print(c.send(1))
print(c.send(2))
print(c.send(3))
 
try:
    c = delayed_coroutine(1.2)
except TimeoutError:
    print('succesful')