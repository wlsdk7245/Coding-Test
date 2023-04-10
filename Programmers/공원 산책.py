# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    answer = []
    
    dx = {"N": -1, "S": 1, "W": 0, "E": 0}
    dy = {"N": 0, "S": 0, "W": -1, "E": 1}
    
    heightPark = len(park)
    widthPark = len(list(park[0]))
    
    x, y = 0, 0
    nx, ny = 0, 0
    
    for i in range(heightPark):
        for j in range(widthPark):
            if park[i][j] == 'S':
                x, y = i, j
                nx, ny = i, j

    for d in routes:
        op, n = d.split()
        n = int(n)
        count = 0
                
        while n:
            nx, ny = nx + dx[op], ny + dy[op]
            n -= 1

            if 0 <= nx < heightPark and 0 <= ny < widthPark:
                if park[nx][ny] == 'X':
                    print('X')
                    nx, ny = x, y
                    break
            else:
                nx, ny = x, y
                break
                
        x, y = nx, ny
                    
    answer.append(x)
    answer.append(y)
    return answer