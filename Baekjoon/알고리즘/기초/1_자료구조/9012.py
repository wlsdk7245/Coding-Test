import sys
N = int(sys.stdin.readline())

for i in range(N):
    num = 0
    arr = sys.stdin.readline()
    for j in arr:
        if j=='(':
            num += 1
        elif j==')':
            num -= 1
        if num < 0:
            break
    if num == 0:
        print('YES')
    else:
        print('NO')