def solution(s):
    dic = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    
    answer = ''
    stack = ''
    
    for i in range(len(s)):
        x = s[i]
        
        if x.isdecimal():
            answer += x
        
        else:
            stack += x          
            if stack in dic:
                answer += dic[stack]
                stack = ''
            
    return int(answer)