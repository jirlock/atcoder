x,y = [int(x) for x in input().split()]

flag = True
count = 1

while flag:
    if x * 2 <= y:
        x = x * 2
        count += 1
        continue
    else:
        flag = False

print(count)