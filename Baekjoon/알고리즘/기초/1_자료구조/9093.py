import sys
N = int(sys.stdin.readline())

for i in range(N):
    sentence = sys.stdin.readline().split()
    for word in sentence:
        print(word[::-1], end=" ")
    print('')