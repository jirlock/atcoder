import sys
sys.setrecursionlimit(1000000)

n, m = map(int,input().split())

a = [[] for _ in range(n)]

for _ in range(m):
    l, r, d = map(int,input().split())
    a[l-1].append((r-1,d))
    a[r-1].append((l-1,-d))

x = [None for _ in range(n)]

def check(y):
    for z,d in a[y]:
        if x[z] is None:
            x[z] = x[y] + d
            if not check(z):
                return False
        elif x[z] != x[y] + d:
            return False
    return True

for i in range(n):
    if x[i] is None:
        x[i] = 0
        if not check(i):
            print('No')
            exit(0)
print('Yes')










