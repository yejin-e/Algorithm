def solution(participant, completion):
    p = {}
    
    for name in participant:
        x = 1
        if name in p:
            x = p[name]+1
        p[name] = x
        
    for name in completion:
        p[name] -= 1
    
    for name in p:
        if p[name] == 1:
            return name  