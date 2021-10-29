import sys
import math

N, M = map(int, sys.stdin.readline().split())


def prime(a):
    if a == 1:
        return False

    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


for num in range(N, M + 1):
    if prime(num):
        print(num)
