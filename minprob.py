x, k = map(int,input().split())

ans = (10 ** k) * (x // (10 ** k) + 1)

print(ans)