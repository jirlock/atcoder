n = int(input())

t_now = 0
p = (0,0)
ans = True

for _ in range(n):
    t,x,y = map(int,input().split())
    td = t - t_now
    d = abs(p[0]-x) + abs(p[1]-y)
    tmp = td - d
    if tmp >= 0 and tmp % 2 == 0:
        t_now = t
        p = (x,y)
        continue
    else:
        ans = False
        break

if ans:
    print('Yes')
else:
    print('No')