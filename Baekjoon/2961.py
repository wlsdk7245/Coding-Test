# 2961 도영이가 만든 맛있는 음식

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

minValue = 1e9 # 최소값을 저장하는 변수
temp = []

def calculate(numbers):
    totalS, totalB = 1, 0
    for n in numbers: # 선택한 전체 재료들 하나하나 순회
        totalS *= n[0] # 신맛은 곱해줌
        totalB += n[1] # 쓴맛은 더해줌

    return abs(totalS - totalB) # 신맛과 쓴맛의 차이를 반환

def dfs(m, start):
    global minValue
    if len(temp) == m: # 재료를 모두 선택함
        minValue = min(calculate(temp), minValue)
        # 신맛과 쓴맛의 차이의 최소값을 저장
        return

    for i in range(start, n): # 같은 재료를 선택할 수 없기에 이를 고려해
        temp.append(arr[i])
        dfs(m, i + 1)
        temp.pop()

for i in range(1, n + 1): # n개중의 재료 중 몇 개를 사용할지
    dfs(i, 0)

print(minValue)