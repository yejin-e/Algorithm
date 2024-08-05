def solution(n):
    answer = ''
    num = [0 for _ in range(10)]
    
    for x in str(n):
        num[int(x)] += 1
    
    for i in range(9,-1,-1):        
        if num[i] != 0:
            answer += str(i) * num[i]
    return int(answer)