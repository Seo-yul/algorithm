"""
방향 그래프에서 최단경로를 구하고자 한다.그래프에 대한 정보들로는 각 노드로부터 간선이 연결된 정보가 딕셔너리 a로 주어진다.
이 때 시작 노드(start)에서 마지막 노드(final)까지의 최소비용을 구하시오.

                               a	                                      start	 final	return
{'A': {'B': 2, 'C': 5, 'D': 1}, 'B': {'C': 8}, 'C': {}, 'D': {'C': 3}}	  'A'	 'C'	  4
"""
import heapq
def solution(a, start, final):
    price = {node: float('inf') for node in a}
    price[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        current_price, current_node = heapq.heappop(queue)

        if price[current_node] < current_price:
            continue

        for adjacent, p in a[current_node].items():
            distance = current_price + p

            if distance < price[adjacent]:
                price[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return price[final]

print(solution({'A': {'B': 2, 'C': 5, 'D': 1}, 'B': {'C': 8}, 'C': {}, 'D': {'C': 3}}, 'A', 'C'))