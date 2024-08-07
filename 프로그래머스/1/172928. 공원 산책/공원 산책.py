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
            sx -= n                        # 일단 해당 위치로 이동
            for k in range(n):             # 해당 위치에서 이전 위치까지 하나씩 돌아보며       
                if park[sx+k][sy] == "X":  # 장애물 만남 체크
                    sx += n                # 만나면 이동 취소
                    break
                
                
        if op == "S" and sx+n < h :
            sx += n
            for k in range(n):          
                if park[sx-k][sy] == "X":
                    sx -= n
                    break
                    
        if op == "W" and sy-n >= 0:
            sy -= n
            for k in range(n):              
                if park[sx][sy+k] == "X":
                    sy += n
                    break
                           
        if op == "E" and sy+n < w:
            sy += n
            for k in range(n):               
                if park[sx][sy-k] == "X":
                    sy -= n
                    break
                    
    return sx, sy                