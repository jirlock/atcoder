x,y = [int(x) for x in input().split()]

count = 1

while True:
    if x * 2 <= y:
        x = x * 2
        count += 1
    else:
        break

print(count)
