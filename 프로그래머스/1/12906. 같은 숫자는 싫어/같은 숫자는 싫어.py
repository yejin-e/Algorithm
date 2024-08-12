def solution(arr):
    answer = []
    for x in arr:
        if answer[-1:] != [x]:    #빈배열일 때 [-1:] 오류 無, [-1] 오류 有
            answer.append(x)        
    return answer