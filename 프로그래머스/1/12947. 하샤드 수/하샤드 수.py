def solution(x):
    s = 0
    y = x
    while x>0:
        s += x%10
        x //= 10 
    return False if y%s else True