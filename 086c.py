from collections import defaultdict

n, k = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

d = defaultdict(int)

for x in a:
    d[x] += 1

e = sorted(d.items(), key=lambda v:v[1])

m = len(e)

ans = 0

if m-k >= 0:
    for i in range(m-k):
        ans += e[i][1]

print(ans)
