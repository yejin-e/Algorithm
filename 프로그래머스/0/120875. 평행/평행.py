def solution(dots):
    x0, y0 = dots[0]
    x1, y1 = dots[1]
    x2, y2 = dots[2]
    x3, y3 = dots[3]
    
    if (y0-y1) / (x0-x1) == (y2-y3) / (x2-x3):
        return 1
    elif (y0-y2) / (x0-x2)  == (y1-y3) / (x1-x3):
        return 1
    elif (y0-y3) / (x0-x3) == (y1-y2) / (x1-x2):
        return 1  
    
    return 0

