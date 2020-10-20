"""
마을에 1부터 N의 고유 번호를 가진 사람들이 있다.
소문으로는 마을 사람 중에 마을 판사가 있다고 한다.
마을 판사가 실제로 존재한다면,

마을 판사는 아무도 믿지 않는다.
다른 모든 사람들은 마을 판사를 믿는다.
마을 판사가 있다면 오직 한명 뿐이다.

리스트 trust가 주어졌을 때,
trust[i] = [a, b]는 고유 번호가 a인 사람이 고유 번호가 b인 사람을 믿는다는 것을 의미한다고 한다.

마을 판사가 존재한다면 마을 판사의 고유 번호를, 존재하지 않는다면 -1을 출력하는 프로그램을 작성하시오.

예시입력

N	trust	출력
2	[[1,2]]	2
3	[[1,3],[2,3]]	3
3	[[1,3],[2,3],[3,1]]	-1
3	[[1,2],[2,3]]	-1
4	[[1,3],[1,4],[2,3],[2,4],[4,3]]	3

"""
from collections import defaultdict

def ck(number, dic):
    return_dic = dict()
    for n in range(number):
        count = len(dic[n+1])
        return_dic[n+1] = count
    return return_dic

def solution(N, trust):
    to_trust = defaultdict(list)
    from_trust = defaultdict(list)

    for t in trust:
        if to_trust[t[0]]:
            to_trust[t[0]].append(t[1])
        else:
            to_trust[t[0]] = [t[1]]

        if from_trust[t[1]]:
            from_trust[t[1]].append(t[0])
        else:
            from_trust[t[1]] = [t[0]]

    to_trust = ck(N, to_trust)
    from_trust = ck(N, from_trust)
    for number in range(N):
        if to_trust[number+1] == 0 and from_trust[number+1] == N-1:
            return number+1
    return -1


print(solution(2, [[1,2]]))
print(solution(3, [[1,3],[2,3]]))
print(solution(3, [[1,3],[2,3],[3,1]]))
print(solution(3, [[1,2],[2,3]]))
print(solution(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))