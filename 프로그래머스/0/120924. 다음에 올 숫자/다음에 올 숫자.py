def solution(common):
    a, b, c = common[:3]
    
    if b - a == c - b:        # 등차수열
        return b - a + common[-1]
    elif b // a == c // b:    # 등차수열
        return b // a * common[-1]