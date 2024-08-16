def solution(array):
    lst = [0]*1000
    num = -1
    cnt = 0
    
    for x in array:
        lst[x] += 1
        
    mode = max(lst)    # 빈도수
    
    for x in range(1000):
        if lst[x] == mode:
            num = x    # 최빈값
            cnt += 1
            if cnt > 1:
                return -1 
            
    return num