"""
n개의 노드가 있는 그래프가 있다.
각 노드는 1부터 n까지 번호가 적혀있다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 한다.
가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미한다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때,
1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성하라.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
입출력 예

n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
"""
from collections import defaultdict
import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])


    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent in graph[current_node]:
            distance = current_distance + 1

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

def solution(n, vertex):
    graph_dict = defaultdict(list)
    for i in vertex:
        graph_dict[i[0]].append(i[1])
        graph_dict[i[1]].append(i[0])

    # print(graph_dict)
    result_dict = dijkstra(graph_dict, 1)
    # print(result_dict)

    # t = heapq.heappush()
    # t = heapq.heapify(result_dict)
    # print(t)
    res = sorted(result_dict.items(), key= lambda x: x[1], reverse=True)
    # print(res)
    k, v = max(res, key= lambda x: x[1])
    answer = 0
    for item in res:
        if item[1] == v:
            answer += 1

    return answer




print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))