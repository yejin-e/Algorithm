def solution(lines):    
    answer = 0   
    start = min(lines[i][0] for i in range(3))
    end = max(lines[i][1] for i in range(3))
    
    arr1 = [0] * (end-start+1)
    arr2 = [0] * (end-start+1)
    arr3 = [0] * (end-start+1)
    
    arr1[lines[0][0]-start:lines[0][1]-start] = [1] * (lines[0][1]-lines[0][0])
    arr2[lines[1][0]-start:lines[1][1]-start] = [1] * (lines[1][1]-lines[1][0])
    arr3[lines[2][0]-start:lines[2][1]-start] = [1] * (lines[2][1]-lines[2][0])
    
    for i in range(end-start+1):
        x = arr1[i] + arr2[i] + arr3[i] 
        if x > 1:
            answer += 1
    return answer