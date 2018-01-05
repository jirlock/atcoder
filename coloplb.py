n, x = [int(x) for x in input().split()]

s = input()

ans = 0

for i in range(n):
    t = int(input())
    if s[i] == '0':
        ans += t
    else:
        ans += min(t,x)

print(ans)
