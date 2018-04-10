# exercise2_1 Calculate the length of the hypotenuse in a right triangle

side_1 = 179
side_2 = 971

side_3 = ((side_1**2) + (side_2**2))**0.5
print(int(side_3))

# exercise2_2 Find the number of tens in a two-digit number
n = int(input())
print(n // 10 % 10)

# exercise2_3 Find the sum of the digits in a three-digit number
number = int(input())

a = number // 100
b = number % 100 // 10
v = number % 10
print(a + b + v)

# exercise2_4 Print the next even number
num = int(input())
t = num % 2

if t == 0:
    print(num + 2)
else:
    print(num + 1)

# exercise2_5 Print the fractional part
f = 872.345
f_1 = f % 1
print(f_1)

# exercise2_6 The first digit after the decimal point
enter_number = float(input())
print(int(10 * (enter_number - int(enter_number))))
