n = int(input())

def over(start, i):
    #return the time of the first train that leaves after the start time of the ith station.
    #when f * (n-1) < start <= f * n, return f * n
    f_ = f[i]
    if start % f_ == 0:
        return start
    else:
        return f_ * ((start // f_) + 1)


c,s,f = [], [], []

times = []

for _ in range(n-1):
    c_, s_, f_ = [int(x) for x in input().split()]
    _ = [x.append(y) for x,y in [(c,c_),(s,s_),(f,f_)]]

for i in range(n-1):
    start = 0
    for j in range(n-1-i):
        tmp = over(start,i+j)
        if tmp < s[i+j]:
            tmp = s[i+j]
        start = tmp + c[i+j]
    times.append(start)

for x in times:
    print(x)
print(0)