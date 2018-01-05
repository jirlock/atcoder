s = input()

x, y = [int(x) for x in input().split()]

is_horizontal = False
count = 0
horizontal = []
vertical = []
first_count = 0

for i,z in enumerate(s):
    if z == 'F':
        first_count += 1
    else:
        x = x - first_count
        s = s[i+1:]
        break

for z in s:
    if z == 'F':
        count += 1
    else:
        count = 0
        if is_horizontal:
            if count != 0:
                horizontal.append(count)
            is_horizontal = False
        else:
            if count != 0:
                vertical.append(count)
            is_horizontal = True

def can_make(n, l):
    #returns if it's possible to make n from l(list) by adding and subtracting
    #dp
    



