def solution(n):
    if n == 0 or n == 1:
        return n
    
    answer = n+1
    for x in range(2, n//2+1):
        if n % x == 0:
            answer += x
    return answer