def solution(keyinput, board):
    answer = [0, 0]
    key = {"left": [-1, 0], "right": [1, 0], "up": [0, 1], "down": [0, -1]}
    
    for k in keyinput:
        
        if abs(answer[0] + key[k][0]) <= board[0]//2 and abs(answer[1] + key[k][1]) <= board[1]//2:
            answer[0] += key[k][0]
            answer[1] += key[k][1]
        
    return answer