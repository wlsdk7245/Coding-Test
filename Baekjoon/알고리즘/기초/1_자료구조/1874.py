n = int(input())
num = [int(input()) for _ in range(n)] # 사용자 지정 순열
cnt = 1

stack = [] # 스택
result = [] # 결과값
temp = True

for i in num:
    while cnt <= i:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if stack[-1] == i:
        stack.pop()
        result.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for _ in result:
        print(_)
