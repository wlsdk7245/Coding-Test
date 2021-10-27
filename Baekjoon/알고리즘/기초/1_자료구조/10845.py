import sys

N = int(sys.stdin.readline())
Q = []

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        Q.append(command[1])
    elif command[0] == 'pop':
        if len(Q) != 0:
            print(Q.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(Q))
    elif command[0] == 'empty':
        if len(Q) != 0 :
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(Q) != 0:
            print(Q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(Q) != 0:
            print(Q[-1])
        else:
            print(-1)