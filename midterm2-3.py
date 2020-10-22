"""
그래프를 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력:
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력:
V부터 방문된 점을 순서대로 출력한다.

예시 입출력

N	M	V	edges	return
4	5	1	[[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]	1 2 3 4

"""
import sys
from collections import deque, defaultdict

N, M, V = 4, 5, 1
edges = [[1, 4], [1,2], [3, 4]]

def solution(N, M, V, edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    def bfs(start):
        visited, need_visit = list(), deque()
        need_visit.appendleft(start)

        while need_visit:
            node = need_visit.popleft()
            if node not in visited:
                visited.append(node)
                need_visit.extendleft(sorted(graph[node], reverse=True))

        return visited

    print(bfs(V))

solution(N, M, V, edges)