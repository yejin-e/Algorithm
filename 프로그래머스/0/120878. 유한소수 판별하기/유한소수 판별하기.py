def solution(a, b):
    b //= GCD(a, b)    # 최대공약수    
    if b == 1:
        return 1
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5     
    return 1 if b == 1 else 2


def GCD(p, q):         # 유클리드호제법
    print(p, q)
    if q == 0: 
        return p
    return GCD(q, p%q)