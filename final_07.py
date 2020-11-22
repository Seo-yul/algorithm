"""
연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다. 이 게임은 브라운이 코니를 잡거나,
코니가 너무 멀리 달아나면 끝난다. 게임이 끝나는데 걸리는 최소 시간을 구하시오.

조건

코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.
출력 형식

브라운이 코니를 잡을 수 있는 최소시간 N초를 표준 출력한다. 단 브라운이 코니를 잡지 못한 경우에는 -1을 출력한다.
예제 입력

C	B	출력
11	2	5
예제 설명

코니의 위치: 11 → 12 → 14 → 17 → 21 → 26
브라운의 위치: 2 → 3 → 6 → 12 → 13 → 26
브라운은 코니를 5초 만에 잡을 수 있다.
"""
from collections import deque


def solution(conyPosition, brownPosition):
    time = 0
    visit = [[0] * 2 for _ in range(200001)]
    q = deque()
    q.append((brownPosition, 0))

    while 1:
        conyPosition += time

        if conyPosition > 200000:
            return -1
        if visit[conyPosition][time % 2]:
            return time

        for i in range(0, len(q)):
            current = q.popleft()
            currentPosition = current[0]
            newTime = (current[1] + 1) % 2

            newPosition = currentPosition - 1
            if newPosition >= 0 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))

            newPosition = currentPosition + 1
            if newPosition < 200001 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))

            newPosition = currentPosition * 2
            if newPosition < 200001 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))
        time += 1