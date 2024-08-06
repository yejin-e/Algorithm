def solution(bandage, health, attacks):
    answer = health                               # 현재 체력
    cnt = 0
    
    for a, b in attacks:       
        cnt = a - cnt - 1                          # 이전 공격으로부터 소요된 시간 
        answer += bandage[1] * cnt                 # 초당 회복량 계산
        answer += bandage[2] * (cnt//bandage[0])   # 추가 회복량 계산
        if answer > health:
            answer = health            
        answer -= b
        if answer < 1:
            return -1
        cnt = a
    return answer