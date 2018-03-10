def dist(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

h,w,d = map(int, input().split())

m = [0 for _ in range(h*w + 1)]
acm = [0 for _ in range(h*w + 1)]
ans = []

for i in range(h):
    a = [int(x) for x in input().split()]
    for j,k in enumerate(a):
        m[k] = (i,j)

for i in range(1, d+1):
    count = i
    while count <= h * w:
        if count <= d:
            pass
        else:
            acm[count] = dist(m[count],m[count-d]) + acm[count-d]
        count += d

q = int(input())

for i in range(q):
    l,r = map(int, input().split())
    ans.append(acm[r] - acm[l])

for x in ans:
    print(x)             



