def solution(num, total):
    answer = []
    
    t = total // num    # answer의 중앙값
    a = num // 2        # 좌우로 연속할 개수
    for n in range(t-a, t+a+1):
        answer.append(n)
    
    if num%2 == 0:    # 짝수개
        x = sum(answer) - total      
        if x == answer[0]:
            del answer[0]
        elif x == answer[-1]:
            del answer[-1]
               
    return answer
