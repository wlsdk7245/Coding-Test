# 15654 N과 M (6)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []

def dfs(startIndex):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    
    for i in range(startIndex, n):
        s.append(arr[i])
        dfs(i + 1)
        s.pop()

dfs(0)