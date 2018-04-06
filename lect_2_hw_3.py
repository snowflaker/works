x = input("Enter year: ")
x = int(x)

t = x % 4
n = x % 400
z = x % 100

if t != 0:
    print("No")
elif z == 0:
    if n == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")


