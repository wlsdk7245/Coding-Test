N = int(input())
num = map(int, input().split())


def prime(a):
    if a == 1:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True


cnt = 0
for j in num:
    if prime(j):
        cnt += 1

print(cnt)
