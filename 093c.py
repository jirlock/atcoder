n = int(input())

a = [int(x) for x in input().split()]

b = []

s = 0

for i in range(n-1):
    b.append(abs(a[i] - a[i+1]))

