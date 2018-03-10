s = input()

if s[:3] == 'yah':
    tmp = s[3:]
    if tmp[0] == tmp[1]:
        flag = True
    else:
        flag = False
else:
    flag = False

if flag:
    print('YES')
else:
    print('NO')