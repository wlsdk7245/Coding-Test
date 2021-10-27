N, K = map(int, input().split())

string = [i for i in range(1, N+1)]
result = []

cnt = K - 1

while len(string):
    if cnt >= len(string):
        cnt = cnt % len(string)
    else:
        result.append(str(string.pop(cnt)))
        cnt += (K-1)

print("<", ", ".join(result), ">", sep="")