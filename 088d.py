h,w = map(int, input().split())

smap = [list(input()) for _ in range(h)]
cmap = [[float('inf') for _ in range(w)] for _ in range(h)]
queue = [(0,0)]
l = [(1,0), (-1,0), (0,1), (0,-1)]

smap[0][0] = '#'

initial_whites = 0

for x in smap:
    for y in x:
        if y == '.':
            initial_whites += 1

cmap[0][0] = 0

while queue:
    v = queue.pop(0)
    for x in l:
        y = (v[0]+x[0], v[1]+x[1])
        if 0 <= y[0] <= h-1 and 0 <= y[1] <= w-1:
            if smap[y[0]][y[1]] == '.':
                smap[y[0]][y[1]] = '#'
                cmap[y[0]][y[1]] = cmap[v[0]][v[1]] + 1
                queue.append(y)
            else:
                pass
        else:
            pass

if cmap[h-1][w-1] == float('inf'):
    print(-1)
else:
    print(initial_whites - cmap[h-1][w-1])

