a, b = map(int, input().split())

def GCD(A, B):
    while B > 0:
        A = A % B
        A, B = B, A
    return A

if a < b:
    temp = a
    a = b
    b = temp

print(GCD(a, b))
print(int(a*b/GCD(a, b)))