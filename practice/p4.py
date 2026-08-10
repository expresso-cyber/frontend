# Q1) Accept the percentage from the user and display the grade according to the following criteria:

# Below 25 —- D
# 25 to 45 —- C
# 45 to 50 —- B
# 50 to 60 –– B+
# 60 to 80 — A
# Above 80 –- A+

m = int(input("Enter Marks: "))

if(m>80 and m<100):
    print("A+")
elif(m>60 and m<=80):
    print("A")
elif(m>50 and m<=60):
    print("B+")
elif(m>45 and m<=50):
    print("B")
elif(m>25 and m<=45):
    print("C")
elif(m<=25 and m>=1):
    print("D")
else:
    print("Invalid Number!")


print("---------------------------------------------------")

# Q2) Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.



print("---------------------------------------------------")

# Q3) Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
# (hint : any number % 10 will return the last digit)

num = int(input("Enter Number: "))
temp = num
lastDig = temp % 10

if(lastDig % 3 == 0):
    print(f"The last digit of the number {num} (i.e {lastDig}) is Divisible by 3")
else:
    print("It is not divisible by 3")


print("---------------------------------------------------")


# Q4) Convert month name to a number of days(if else)

month = input("Enter month name: ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("31 Days")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("30 Days")
elif month == "February":
    print("28 Days (or 29 In leap year)")
else:
    print("Invalid month name.")

print("------------------------------------------------------------")


# Q5) Take input from the user and find the second largest number (middle value) of three Numbers



print("------------------------------------------------------------")


# Q6) Python program to enter week number and print day of week

day = 7

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else: 
    print("Invalid Day!")


print("------------------------------------------------------------")


# Q7) Python program to check vowel.




print("------------------------------------------------------------")


# Q8) Python program to find maximum between three numbers

x,y,z = 2,1,0

max = 0

if(x>y and x>z):
    max = x
elif(y>x and y>z):
    max = y
elif(z>y and z>x):
    max = z
    
print(f"{max} is maximum between {x}, {y} and {z}")