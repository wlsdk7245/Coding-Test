# 11663 선분 위의 점

n, m = map(int, input().split())

dots = list(map(int, input().split()))
dots.sort()

lines = [list(map(int, input().split())) for _ in range(m)]

def left(a):
    start, end = 0, n - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if dots[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    
    return end + 1

def right(a):
    start, end = 0, n - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if dots[mid] > a:
            end = mid - 1
        else:
            start = mid + 1
    
    return end

for line in lines:
    answer = 0
    start, end = line
    print(right(end) - left(start) + 1)