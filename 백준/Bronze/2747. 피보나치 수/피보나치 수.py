import sys


def fibo(a, b, n):
    if n == 0:
        return b
    return fibo(b, a+b, n-1)


n = int(sys.stdin.readline())
a = 0
b = 1
print(fibo(a, b, n-1))
