n, k = map(int,input().split())

ans = 0

for b in range(1, n + 1):
    ans += ((n+1)//b)*max(0,b-k) + max(0,((n+1)%b)-k)
    if k == 0:
        ans -= 1

print(ans)
