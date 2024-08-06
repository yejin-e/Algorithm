def solution(num):  
    answer = 0
    
    while answer < 500:
        if num == 1:
            return answer
        elif num % 2:    # 홀수
            num = (num * 3 + 1)//2
            answer += 2
        else:          # 짝수
            num //= 2
            answer += 1
            
    return -1