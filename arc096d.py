n, c = map(int, input().split())

#lx and lux are lists of distances
lx, lv = [], []
for _ in range(n):
    tmpx, tmpv = map(int, input().split())
    lx.append(tmpx)
    lv.append(tmpv)
lux = [c-x for x in reversed(lx)]

#sum of sushi
tmpv1, tmpv2 = 0,0
vc, vuc = [],[]
for i in range(n):
    tmpv1 += lv[i]
    tmpv2 += lv[n-1-i]
    _ = [x.append(y) for x,y in zip([vc,vuc],[tmpv1,tmpv2])]

#energy
sc, suc = [],[]
tmp1,tmp2 = 0,0
for i in range(n):
    sc.append(vc[i] - lx[i])
    suc.append(vuc[i] - (c - lx[n-1-i]))

#max of energy until ith sushi
ssc,ssuc = [],[]
tmp,tmpu = -c, -c
for i in range(n):
    tmp = max(tmp, sc[i])
    tmpu = max(tmpu, suc[i])
    ssc.append(tmp)
    ssuc.append(tmpu)
ans = 0

for i in range(n):
    s1 = sc[i]
    s2 = suc[i]
    if i == n-1:
        s3,s4 = 0,0
    else:
        s3 = s1 - lx[i] + ssuc[max(0,n-i-2)]
        s4 = s2 - lux[i] + ssc[max(0,n-i-2)]

    ans = max(ans,s1,s2,s3,s4)

print(ans)
