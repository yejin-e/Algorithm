import sys

while True:
    n = sys.stdin.readline()
    if n == '':
        break
        
    n = int(n)
    x = 1
    s = 1
    while s % n != 0:
        x += 1
        s = int('1' * x)
    print(x)
