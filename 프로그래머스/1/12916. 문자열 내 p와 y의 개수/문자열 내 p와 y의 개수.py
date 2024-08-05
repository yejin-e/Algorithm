def solution(s):
    a = 0
    b = 0
    
    for c in s:
        if c == 'p' or c == 'P':
            a += 1
        elif c == 'y' or c == 'Y':
            b += 1
            
    return (a==b)