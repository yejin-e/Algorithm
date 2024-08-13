def solution(numer1, denom1, numer2, denom2):  
    denom = denom1 * denom2 // comparison(denom1, denom2)    # 최소공배수를 사용해 공통 분모 
    numer = denom // denom1 * numer1 + denom // denom2 * numer2    # 덧셈한 분자
    
    x = comparison(numer, denom)    # 덧셈 분수의 기약 분수
    return [numer//x, denom//x]


def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a%b)


def comparison(a, b):
    max_num = max(a, b)
    min_num = min(a, b)
    return GCD(max_num, min_num)
    

# 최대공약수 = z   GCD
# a % b = c
# b % c = d
# ...
# y % z = 0

# 최소공배수 = z    LCM
# (a * b) / 최대공약수(a, b) = z