"""
아래와 같은 기능을 가진 Foo 클래스를 완성하시오.

Foo 클래스는 초기화 시 여러개의 정수를 입력으로 받는다. 정수의 개수는 정해져있지 않다.
Foo 클래스의 인스턴스는 print()에 입력될 경우 '입력받은 모든 정수의 합'을 출력한다.
Foo 클래스로 생성된 객체들은 sort를 이용해 정렬할 수 있으며, 정렬할 때에는 '입력받은 모든 정수의 곱'을 기준으로 한다.
Foo 클래스의 인스턴스끼리 더할 경우, 두 인스턴스의 초기화에 사용된 정수들을 모두 입력받아 생성된 인스턴스를 리턴한다.
"""
from functools import reduce

class Foo:
    def __init__(self, *input_data):
        self._input_data = input_data

    def __str__(self):
        return str(sum(self._input_data))

    def __add__(self, other):
        tmp = self._input_data + other._input_data
        r = Foo(*tmp)
        return r
    
    def __lt__(self,other):
        s = reduce (lambda x,y:x*y, self._input_data)
        o = reduce (lambda x,y:x*y, other._input_data)

        if s < o: return True
        else: return False
    

a = Foo(1,2,3)
b = Foo(4,5,6)
print(a + b)
c = Foo(1,2,3,4,5,6)
print(c)

d =  [Foo(1,2,3), Foo(4,5,6), Foo(0,2,3)]
print('id: {}'.format(d))
d.sort()
print('id: {}'.format(d))