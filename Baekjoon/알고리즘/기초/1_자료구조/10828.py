import sys

input = sys.stdin.readline
N = int(input())

arr = []

for i in range(N):
    request = sys.stdin.readline().split()
    if request[0] == 'push':
        arr.append(request[1])
    elif request[0] == 'pop':
        try:
            print(arr.pop())
        except:
            print('-1')
    elif request[0] == 'size':
        print(len(arr))
    elif request[0] == 'empty':
        if len(arr) == 0:
            print('1')
        else:
            print('0')
    elif request[0] == 'top':
        try:
            print(arr[-1])
        except:
            print('-1')