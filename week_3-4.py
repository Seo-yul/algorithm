"""
데코레이터 함수의 이름은 wrapper_func으로 한다.
데코레이터가 적용될 함수의 입력 인자의 개수는 임의의 개수에 대해서 동작해야 한다.
데코레이터는 함수를 실행하기 전에 아래와 같은 동작을 한다.
함수의 이름과 함수에 입력된 인자의 개수를 출력한다.
함수를 실행할 때에 모든 입력 인자가 정상적으로 전달되어야 한다.
데코레이터는 함수를 실행한 후에 아래와 같은 동작을 한다.
함수를 실행한 후에, 함수가 실행되는데 걸린 시간을 출력한다.
함수가 10초 이상 동작한 경우, 경고 메세지를 출력한다.
데코레이터를 적용하더라도 함수의 반환값은 정상적으로 반환되어야 한다.
"""

# 과제 4번 코드란
import time
import logging

def wrapper_func(func):

    def deco_closer_func(*args):
        name = func.__name__
        args_len = len(args)
        print('함수의 이름: {}\n인자의 개수: {}'.format(name, args_len))

        start_time = time.perf_counter()
        func_result = func(*args)
        end_time = time.perf_counter()

        calc_time = (int(end_time - start_time)*100)/100
        print('실행 소요 시간 : {}'.format(calc_time))

        if calc_time >= 10:
            logging.warning('실행시간이 10초를 넘었습니다!')
        

        return func_result

    return deco_closer_func


@wrapper_func
def time_func(seconds):
    time.sleep(seconds)
    return print('time_func 끝')


time_func(11)
