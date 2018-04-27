n, x = map(int, input().split())

def aaa(a,b):
    n = max(a,b)
    m = min(a,b)
    if n % m == 0:
        return 2 * n - m
    else:
        return 2 * m * int(n / m) + aaa(m, n % m)

ans = n + aaa(n-x, x)

print(ans)
