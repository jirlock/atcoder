n = input()

a = n[0]

if len(n) > 1:
    b = n[1:]
    if (int(b)+1) % (10 ** len(b)) == 0:
        flag = True
    else:
        flag = False
else:
    b = ''
    flag = True

if flag:
    ans = int(a) + 9 * len(b)
else:
    ans = int(a) - 1 + 9 * len(b)

print(ans)

