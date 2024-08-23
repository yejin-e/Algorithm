# N개 하노이탑(끝)
# = {N-1개 하노이탑(중간) + 최하단 원판(끝) + N-1개 하노이탑(끝)}
# 재귀로 해결시 타임아웃

def solution(n):
    answer = [[1,2], [1,3], [2,3]]
    
    if n == 1:
        return [[1,3]]
        
    for _ in range(3, n+1):
        arr = answer      # 이전 개수 옮기는 방법
        answer = []       # 현재 개수 옮기는 방법
        
        for i in range(len(arr)):
            if i%2:        # 홀수 인덱스
                answer.append(arr[i])
            else:          # 짝수 인덱스
                a, b = arr[i]
                x = 6-a-b
                answer.append([a, x])
                answer.append(arr[i])
                answer.append([x, b])
                
    return answer