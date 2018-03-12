n, m = map(int,input().split())

if n==1 or m==1:
    if n==1 and m==1:
        print(1)
    else:
        if n == 1:
            print(m-2)
        else:
            print(n-2)
else:
    if n == 2 or m == 2:
        print(0)
    else:
        print((n-2)*(m-2))