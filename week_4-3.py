"""
__slots__를 사용하여 최적화된 클래스를 구현하시오. 아래 조건을 만족하도록 구현하시오.

클래스의 이름은 Vector3D로 한다.
클래스의 멤버 변수는 x, y, z로 한다.
클래스의 사칙연산을 구현한다.
Vector3D 객체끼리의 합과 차는 x, y, z를 각각 합/차를 구해 Vector3D로 반환한다.
Vector3D 객체끼리의 곱은 내적 (x1 * x2 + y1 * y2 + z1 * z2)을 숫자로 반환한다.
Vector3D 객체끼리의 나눗셈은 NaN을 반환한다.
그 외에 모든 경우 NotImplementedError 예외를 발생시킨다.
클래스를 print()로 출력할 경우, 아래 포맷으로 출력한다.
"Vector3D (%.3f, %.3f, %.3f)" % (x, y, z)
아래 주어진 테스트 코드에서 반드시 정상 동작하도록 코드를 작성하시오.
"""
class Vector3D(object):
    __slot__ = ('a', 'b', 'c')
    
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
    
    def __add__(self, other):
        try:
            result = Vector3D( self.x + other.x,\
                            self.y + other.y, \
                            self.z + other.z)
            return result
        except Exception:
            raise NotImplementedError
            

    
    def __sub__(self, other):
        try:
            result = Vector3D( self.x - other.x,\
                            self.y - other.y, \
                            self.z - other.z)
            return result
        except Exception:
            raise NotImplementedError

    def __mul__(self, other):
        try:
            result = self.x * other.x + \
                    self.y * other.y + \
                    self.z * other.z
            return result
        except Exception:
            raise NotImplementedError

    def __truediv__(self, other):
        if type(self) == type(other):
            return None
        raise NotImplementedError
    
    def __floordiv__(self, other):
        if type(self) == type(other):
            return None
        raise NotImplementedError

    def __mod__(self, other):
        if type(self) == type(other):
            return None
        raise NotImplementedError

    def __repr__(self):
        return "Vector3D (%.3f, %.3f, %.3f)" % (self.x, self.y, self.z)

    # def Ex

# # Test code 
a = Vector3D(0.4, 0.6, 0.2)
b = Vector3D(1.2, 0.7, 2.1)
 
print(a + b)
print(a - b)
print(a * b)
print(a / b)
 
try:
    a * 3
except NotImplementedError:
    print('successful')
except:
    pass
 
try:
    a + 2
except NotImplementedError:
    print('successful')
except:
    pass
 
try:
    a / 4
except NotImplementedError:
    print('successful')
except:
    pass