n = int(input())

a = [int(x) for x in input().split()]

a_min = min(a)
a_max = max(a)
a_min_index = 0
a_max_index = 0

for i,x in enumerate(a):
    if x == a_min:
        a_min_index = i+1
    elif x == a_max:
        a_max_index = i+1

if a_min >= 0:
    #累積和
    print(n-1)
    for i in range(1,n):
        print(i, i+1)
else:
    if abs(a_min) <= abs(a_max):
        #all positive
        print(2*n-1)
        for i in range(1, n+1):
            print(a_max_index, i)   
        for i in range(1,n):
            print(i, i+1)
    else:
        #all negative
        print(2*n-1)
        for i in range(1, n+1):
            print(a_min_index, i)
        for i in reversed(range(2,n+1)):
            print(i, i-1)

