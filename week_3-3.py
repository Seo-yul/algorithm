"""
클로저를 반환하는 함수이다.
클로저 함수는 아래와 같은 기능을 한다.
클로저 함수의 외부 영역에 딕셔너리 변수 dict_a를 가진다.
k와 v를 각각 입력 인자로 가진다. v는 항상 정수로 입력된다.
k 값이 딕셔너리의 Key로 사용될 수 없는 경우 None을 리턴한다.
k 값이 딕셔너리의 Key로 유효한 경우 아래와 같은 동작을 한다.
딕셔너리 dict_a에 k, v 쌍을 아래와 같은 규칙으로 입력한다.
k 값은 클로저 함수에 중복으로 들어올 수 있다.
v 값이 처음 입력된 경우 [v]로 입력되며, 다음 v1 값이 입력된 경우 [v, v1] 등으로 리스트에 누적된다.
아래와 같은 딕셔너리dict_b를 출력한다.
dict_b는 dict_a와 동일한 Key를 가진다.
dict_b의 각 Key의 Value는, dict_a의 동일한 Key를 가진 Value 리스트의 총 합이다.
"""
def wrapper_func():
    dict_a = dict()

    def closer_func(k, v: int):
        nonlocal dict_a
 
        if hash(k) is False:
            return None
        dict_a.setdefault(k,[]).append(v)
        dict_b = {key:sum(value) for key, value in dict_a.items()}
        return dict_b

    return closer_func
  
quiz = wrapper_func()
print( quiz('age',10) )
print( quiz('grade', 100) )
print( quiz('age',20) )