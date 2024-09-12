import sys

m = int(sys.stdin.readline().rstrip())
s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for _ in range(m):
    op = sys.stdin.readline().rstrip()

    if op == 'all':
        s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        continue
    elif op == 'empty':
        s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        continue

    op, x = op.split()
    x = int(x)

    if op == 'add':
        s[x-1] = 1
    elif op == 'remove':
        s[x-1] = 0
    elif op == 'check':
        sys.stdout.write(str(s[x-1]) + '\n')
    elif op == 'toggle':
        s[x-1] ^= 1
