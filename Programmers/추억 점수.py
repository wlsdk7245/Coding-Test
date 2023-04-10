# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    data = dict()
    
    
    for i in range(len(name)):
        data[name[i]] = yearning[i]
    
    for p in photo:
        temp = 0
        for n in p:
            if n in data:            
                temp += data[n]
        
        answer.append(temp)
    
    return answer