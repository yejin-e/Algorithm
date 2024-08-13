def solution(common):
    answer = 0
    a = common[0]
    b = common[1]
    c = common[2]
    x = common[-1]
    
    if b - a == c - b:    # 등차수열
        return b - a + x
    elif b // a == c // b:    # 등차수열
        return b // a * x