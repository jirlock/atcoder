a,b,c,x,y = map(int, input().split())

ans = 0

if a + b > 2 * c:
    if x > y:
        if a > 2 * c:
            ans += x * 2 * c
        else:
            ans += y * 2 * c + (x - y) * a
    else:
        if b > 2 * c:
            ans += y * 2 * c
        else:
            ans += x * 2 * c + (y - x) * b
else:
    ans += a * x + b * y

print(ans)