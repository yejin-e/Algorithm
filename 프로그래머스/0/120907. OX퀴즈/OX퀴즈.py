def solution(quiz):
    answer = []
    
    arr = str(quiz)   
    for x in ['[', ']', '\'', ',']:
        arr = arr.replace(x, '')   
    arr = arr.split()
    
    for i in range(0, len(arr)-4, 5):
        a = int(arr[i])
        b = int(arr[i+2])
        c = int(arr[i+4])
        
        x = a + b if arr[i+1] == '+' else a - b        
        answer.append("O" if x == c else "X")
        
    return answer