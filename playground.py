from time import time

a = time()
b = [0 for _ in range(10000)]
for i in range(10000):
    b[i] += i
c = time()
d = []
for j in range(10000):
    d.append(j)
e = time()

print(c - a)
print(e - c)