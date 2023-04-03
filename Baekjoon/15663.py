# 15665 N과 M (9)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []

prev = 0
visited = [False] * n

def dfs(depth):
    prev = 0
    if depth == m:
        print(" ".join(map(str, s)))
        return

    for i in range(n):
        if arr[i] != prev and visited[i] == False:
            s.append(arr[i])
            prev = arr[i]
            visited[i] = True
            dfs(depth + 1)
            s.pop()
            visited[i] = False

dfs(0)