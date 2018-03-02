import numpy as np

l = []

for _ in range(3):
    a = [int(x) for x in input().split()]
    l.append(a)

l = np.array(l)

def check(m):
    a = []
    for i in range(3):
        b,c = m[i,0] - m[i,1], m[i,1] - m[i,2]
        a.append((b,c))
    if a[0] != a[1] or a[1] != a[2]:
        return False
    else:
        return True

if check(l) and check(np.transpose(l)):
    print('Yes')
else:
    print('No')

