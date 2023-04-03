# 15656 N과 M (7)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []

def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    
    for i in range(n):
        s.append(arr[i])
        dfs()
        s.pop()

dfs()