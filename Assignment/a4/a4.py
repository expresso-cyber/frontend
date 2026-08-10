"""
Q1) Accept the percentage from the user and display the grade according to the following criteria:

Below 25 —- D
25 to 45 —- C
45 to 50 —- B
50 to 60 –– B+
60 to 80 — A
Above 80 –- A+

Q2) Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.

Q3) Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
(hint : any number % 10 will return the last digit)

Q4) Convert month name to a number of days(if else)

Q5) Take input from the user and find the second largest number (middle value) of three Numbers

Q6) Python program to enter week number and print day of week

Q7) Python program to check vowel.

Q8) Python program to find maximum between three numbers
"""

# Q1. Accept percentage from the user and display the grade according to the following criteria:

# Below 25 —- D
# 25 to 45 —- C
# 45 to 50 —- B
# 50 to 60 –– B+
# 60 to 80 — A
# Above 80 –- A+

# Solution =>

marks = 45

if (marks>80):
    print("A+")
elif (marks>=60 and marks<80):
    print('A')
elif (marks>=50 and marks<60):
    print('B+')
elif (marks>=45 and marks<50):
    print('B')
elif (marks>=25 and marks<45):
    print('C')
elif (marks<25):
    print('D')
else: 
    print("Enter a valid marks.")

print("--------------------------------------------------------")


# Q2) Accept three sides of a triangle and check whether it is an equilateral

# Solution ==>

x,y,z = 10,10,10

if (x==y and y==z):
    print("Triangle is equilateral triangle.")
else:
    print("Triangle is not equilateral triangle.")


print("--------------------------------------------------------")


# Q3) Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
# (hint : any number % 10 will return the last digit)

num = 1458
l_digit = num % 10

if(l_digit % 3 == 0):
    print("The last digit is divisible.")
else:
    print("The last digit is not divisible.")

print("--------------------------------------------------------")


# Q4) Convert month name to a number of days(if else)

# solution ==>

month = input("Enter month name: ").strip().lower()

if (
    month == "january"
    or month == "march"
    or month == "may"
    or month == "july"
    or month == "august"
    or month == "october"
    or month == "december"
):
    print("The given month has 31 days")
    
elif (
    month == "april"
    or month == "june"
    or month == "september"
    or month == "november"
):
    print("The given month has 30 days")
elif month == "february":
    print("The given month has 28 days")
else:
    print("Invalid month name")


# Q5) Take input from the user and find the second largest number (middle value) of three Numbers

# solution =>

m = int(input("Enter Your Number: "))
n = int(input("Enter Your Number: "))
p = int(input("Enter Your Number: "))

if (m >= n and m <= p) or (m >= p and m <= n):
    print(f"Second largest number is {m}")

elif(n >= m and n <= p) or (n >= p and n <= m):
    print(f"Second largest number is {n}")

else:
    print(f"Second Largest number is {p}")


print("------------------------------------------------------------------------")

# Q6) Python program to enter week number and print day of week
# solution ==>

week_num = int(input("Enter week number (1 to 7): "))

if week_num == 1:
    print("Monday")
elif week_num == 2:
    print("Tuesday")
elif week_num == 3:
    print("Wednesday")
elif week_num == 4:
    print("Thursday")
elif week_num == 5:
    print("Friday")
elif week_num == 6:
    print("Saturday")
elif week_num == 7:
    print("Sunday")
else:
    print("Error!. Enter a valid week number")
    
    
print("-----------------------------------------------------------------------")


# Q7) Python program to check vowel.
# Solution ==>

check_vowel = 'a'

if check_vowel == 'a' or check_vowel == 'e' or check_vowel == 'i' or check_vowel == 'o' or check_vowel == 'u':
    print("The given letter is vowel")
else:
    print("The given number is not a vowel")
    
print("________________________________________________________________________")

# Q8) Python program to find maximum between three numbers
# Solution: 

q,r,s = 10,20,30

max = 0

if(q>=r and q>= s):
    max = q
elif (r>=q and r >= s):
    max = r
else: 
    max = s

print(f"{max} is the maximum between these three numbers.")

