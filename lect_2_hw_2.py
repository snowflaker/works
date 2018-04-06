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

if t == 0 :
    print("Enter an odd number")
else:
    print(num + 1)

# exercise2_5 Print the fractional part
f = 872.345
f_1 = f % 1
print(f_1)

# exercise2_6 The first digit after the decimal point
enter_number = float(input())
int_number = int(enter_number)
if int_number == 0:
    convert_number = enter_number * 10
    end_number = int(convert_number)
    print(end_number)
if int_number > 0:
    print(int(10 * (enter_number - int(enter_number))))
