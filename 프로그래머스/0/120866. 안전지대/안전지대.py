def solution(board):
    answer = 0
    n = len(board[0])
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                if (mine(i-1, j-1, n) and board[i-1][j-1] == 1) or (mine(i-1, j, n) and board[i-1][j] == 1) or (mine(i-1, j+1, n) and board[i-1][j+1] == 1) or (mine(i, j-1, n) and board[i][j-1] == 1) or (mine(i, j+1, n) and board[i][j+1] == 1) or (mine(i+1, j-1, n) and board[i+1][j-1] == 1) or (mine(i+1, j, n) and board[i+1][j] == 1) or (mine(i+1, j+1, n) and board[i+1][j+1] == 1):
                    board[i][j] = 2
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1        
    return answer


def mine(x, y, n):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True