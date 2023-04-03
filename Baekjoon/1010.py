T = int(input())
import math

def solution():
    r, n = map(int, input().split())
    # nCr = n! / r!(n - r)!
    temp = math.ceil(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
    print(temp)
    
for _ in range(T):
    solution()
    