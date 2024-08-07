def solution(park, routes):
    h = len(park)
    w = len(park[0])
    
    for i in range(h):       
        for j in range(w):
            if park[i][j]=="S":
                sx, sy = i, j     # 시작 위치 찾기


    for r in routes:
        op, n = r.split()
        n = int(n)

        if op == "N" and sx-n >= 0:        # 공원 벗어남 체크
            for k in range(1, n+1):        # 이동할 위치까지   
                if park[sx-k][sy] == "X":  # 장애물 만남 체크
                    break
            else:                          # for-else: for문에서 break로 빠져나가면 else문 미실행
                sx -= n                    # 이동 진행
                                
        if op == "S" and sx+n < h :
            for k in range(1, n+1):        
                if park[sx+k][sy] == "X":
                    break
            else:
                sx += n
                    
        if op == "W" and sy-n >= 0:
            for k in range(1, n+1):              
                if park[sx][sy-k] == "X":
                    break
            else:
                sy -= n
                           
        if op == "E" and sy+n < w:
            for k in range(1, n+1):               
                if park[sx][sy+k] == "X":
                    break
            else:
                sy += n
                    
    return sx, sy                