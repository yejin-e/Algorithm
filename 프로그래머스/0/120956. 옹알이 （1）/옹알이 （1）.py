def solution(babbling):
    answer = 0
        
    for babble in babbling:
        flag = True
        i = 0
        
        while flag:
            if babble[i:i+2] == "ye":
                i += 2
                flag = True
            elif babble[i:i+2] == "ma":
                i += 2
                flag = True
            elif babble[i:i+3] == "aya":
                i += 3
                flag = True
            elif babble[i:i+3] == "woo":
                i += 3
                flag = True
            else:
                flag = False
        
            if flag == True and i >= len(babble):
                answer += 1   
                
    return answer