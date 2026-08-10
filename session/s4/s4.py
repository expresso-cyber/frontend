# 1.Arithmetic operators
#  +   -  *   /   %  (** => Exponent)   (//  => floor division)
"""
a = 10
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
"""

# 2.Assignment operators
# =  +=   -=   *=   /=   %=
"""
a = 10
#a += 2     # same as    a = a + 2
#a -= 2     # same as    a = a - 2
a *= 2
a /= 2
a %= 2
a //= 2
a **= 2
print(a)
"""
# 3.Comparsion operators
# ==   !=   >    <    >=   <=
"""
a = 10
b = 10
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
"""
# print(10 == '10')
# print(1 == True)

# 4.Logical operators
# and   or    not()

# condition 1    and   condition 2   = Output
#    T                    T              T

# condition 1    or   condition 2   = Output
#    F                    F              F

# not()
# F => T
# T => F
# a = 10
# b = 5
# print(a > 5 and b > 3)
# print(a < 5 or b < 3)
# print(not(a < 5) or b < 3)
# print((a > b or 10 > 5) and a < b)


# conditional statements
# 1.if else
"""
age = int(input('Enter your age: '))

if (age >= 18):
    print("You can vote")
else:
    print("You can't vote")

"""
"""
num = int(input('Enter your num: '))
if num >= 30:
    print(f"{num} is greater than 30")
elif num >= 20:
    print(f"{num} is greater than 20")
elif num >=10:
    print(f"{num} is greater than 10")
else:
    print(f"{num} is less than 30")
"""

# Q1 Take 2 input from user and print highest number.
"""
num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
if num1>num2:
    print(num1)
else:
    print(num2)
"""
# Q2 Take 1 input from user and check given number is Even or Odd.
"""
num1 = int(input('Num1: '))
if num1 % 2 == 0:
    print('Even')
else:
    print('Odd')
"""
# Q3 Take 1 input from user and check given number is +ve or -ve.
"""
num1 = int(input('Num1: '))
if num1 > 0:
    print('+ve')
else:
    print('-ve')
"""

# Q4 Take 3 input from user and print highest number.
"""
num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
num3 = int(input('Num2: '))

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2 > num3:
    print(num2)
else:
    print(num3)
"""
# Q5 Take 3 input from user and print second highest number.


# Nested if

num = int(input("Num1: "))
if num % 2 == 0:
    if num > 0:
        print("num is even and +ve")
    else:
        print("num is even and -ve")
else:
    if num > 0:
        print("num is Odd and +ve")
    else:
        print("num is Odd and -ve")

print("hi")
