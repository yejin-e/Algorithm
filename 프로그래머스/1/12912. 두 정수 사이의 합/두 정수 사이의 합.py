def solution(a, b):
    if a == b:
        return a
    answer = 0
    maxx = max(a, b)
    minn = min(a, b)
    for n in range(minn, maxx+1):
        answer += n  
    return answer