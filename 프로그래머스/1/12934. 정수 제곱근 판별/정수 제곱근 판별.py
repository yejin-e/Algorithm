from math import sqrt

def solution(n):
    answer = sqrt(n)       
    return (answer+1)**2 if answer%1 == 0 else -1