n = int(input())

a0 = [int(x) for x in input().split()]
a1 = [int(x) for x in input().split()]

ans = 0
s = sum(a1)

for i in range(n):
    s += a0[i]
    if i == 0:
        pass
    else:
        s -= a1[i-1]
    if s > ans:
        ans = s

print(ans)