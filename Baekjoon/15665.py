# 15665 N과 M (11)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []

def dfs(depth):
    if depth == m:
        
        print(*s)
        return
    
    depth += 1
    prev = 0
    
    for i in range(n):
        if prev != arr[i]:
            s.append(arr[i])
            prev = arr[i]
            dfs(depth)
            s.pop()
dfs(0)