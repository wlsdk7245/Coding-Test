def GCD(A, B):
    while B > 0:
        A = A % B
        A, B = B, A
    return A

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    if a < b:
        temp = a
        a = b
        b = temp
    print(int(a*b/GCD(a, b)))