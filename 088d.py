s = input()

l = len(s)

t = l

for i,x in enumerate(s):
    if i == 0:
        pass
    else:
        if x != s[i-1]:
            a = max(i,l-i)
            t = min(t,a)

print(t)