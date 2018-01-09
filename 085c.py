n, y = [int(x) for x in input().split()]

f, t = -1, -1

for i in range(n+1):
    if f != -1:
        break
    else:
        start = 1000 * n + 4000 * i
        for j in range(n-i+1):
            tmp = start + 9000 * j
            if tmp == y:
                f, t = i, j
                break

if f == -1:
    print('-1 -1 -1')
else:
    print(t, f, n-f-t)
