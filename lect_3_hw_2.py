# exercise3_2
a = input()
l = len(a)

if l % 2 == 0:
    c = a[:int(l / 2)]
    v = a[int(l / 2):]
    z = v + c
    print(z)
else:
    c = a[:int(l / 2) + 1]
    v = a[int(l / 2) + 1:]
    z = v + c
    print(z)
