# 1012 유기농 배추

from collections import deque

T = int(input())


def solution(y, x):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if graph[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        solution(x + 1, y)
        solution(x - 1, y)
        solution(x, y + 1)
        solution(x, y - 1)
        return True
    return

for i in range(T):
    m, n, k = map(int, input().split())
    result = 0
    
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if solution(i, j) == True:
                result += 1
    
    print(result)