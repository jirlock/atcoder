mod = 10 ** 9 + 7

n, k = map(int, input().split())

l = [0]
r = [0 for _ in range(10**5 + 1)]
r[0] += 1
w = 1

for _ in range(n):
    a = int(input())
    if r[a] > 0:
        w = (w * 2) % mod
    else:
        r[a] += 1
        tmp = []
        for x in l:
            b = a ^ x
            r[b] += 1
            tmp.append(b)
        l += tmp
if r[k] > 0:
    print(w)
else:
    print(0)


