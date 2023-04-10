# 25858 원상 복구 (small)

n, k = map(int, input().split())

s = list(map(int, input().split()))
d = list(map(int, input().split()))

p = [s[i] for i in range(n)]

for _ in range(k):
    temp = [0 for _ in range(n)]
    for i in range(n):
        temp[d[i] - 1] = p[i]
    
    p = temp

print(*p)