def solution(polynomial):
    xCnt = 0
    numCnt = 0   
    polynomial = polynomial.replace('+', '')
    polynomial = polynomial.split()
    
    for p in polynomial:
        if 'x' in p:
            xCnt += int(p[:-1]) if len(p)!=1 else 1
        else:
            numCnt += int(p)
         
    if xCnt and numCnt:
        return f"x + {str(numCnt)}" if xCnt == 1 else f"{str(xCnt)}x + {str(numCnt)}"
    elif not xCnt:               # 일차항 미존재
        return str(numCnt)
    elif not numCnt:             # 상수항 미존재
        return "x" if xCnt == 1 else f"{str(xCnt)}x"   
    else:
        return 0