from collections import defaultdict

d = defaultdict(int)

ans = 0

n = int(input())

for x in [int(y) for y in input().split()]:
    d[x] += 1

for k,v in d.items():
    if k > v:
        ans += v
    else:
        ans += v - k

print(ans)