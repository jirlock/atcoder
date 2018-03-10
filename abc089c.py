from collections import defaultdict
from itertools import combinations

d = defaultdict(int)

n = int(input())

for _ in range(n):
    initial = input()[0]
    if initial in 'MARCH':
        d[initial] += 1

a = list(d.values())

ans = 0

for x in combinations(range(len(a)),3):
    ans += a[x[0]] * a[x[1]] * a[x[2]]

print(ans)
