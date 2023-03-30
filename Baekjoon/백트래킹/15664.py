# 15665 N과 M ()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []

prev = 0
visited = [False] * n

def dfs(depth, start):
    prev = 0
    if depth == m:
        print(" ".join(map(str, s)))
        return

    for i in range(start, n):
        if arr[i] != prev and visited[i] == False:
            s.append(arr[i])
            prev = arr[i]
            visited[i] = True
            dfs(depth + 1, i)
            s.pop()
            visited[i] = False

dfs(0, 0)