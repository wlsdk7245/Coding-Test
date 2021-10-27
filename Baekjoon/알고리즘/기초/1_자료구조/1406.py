import sys

string = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())

nextStack = []

for _ in range(M):
    command = sys.stdin.readline().strip()

    if command[0] == 'P':
        string.append(command[2])
    elif command[0] == 'L' and string != []:
        nextStack.append(string.pop())
    elif command[0] == 'D' and nextStack != []:
        string.append(nextStack.pop())
    elif command[0] == 'B' and string != []:
        string.pop()

print(''.join(string + list(reversed(nextStack))))