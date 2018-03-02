import numpy as np

n,k = map(int,input().split())

k_ = 2 * k

a = np.zeros((k_,k_), dtype=np.int)

for _ in range(n):
    x_,y_,c_ = input().split()
    x = int(x_) % k_
    y = int(y_) % k_
    if c_ == 'B':
        a[x,y] += 1
    else:
        a[x,y-k] += 1

ans = 0

for i in range(k_):
    for j in range(k):
        #create a matrix and take the inner product
        b = np.zeros((4*k,4*k), dtype=np.int)
        #(i,j),(i-k,j-k),(i-k,j+k),(i+k,j-k),(i+k,j+k)
         
        



print(int(ans))

