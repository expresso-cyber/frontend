# Q1)Write a While loop which appends the square of each number to the new list.

# Solution ==>
li=[1,2,3,4,5,7,9]

i = 0

li1 = []

while i<len(li):
    s_num = li[i]**2
    li1.append(s_num)
    i += 1

print(li1)

print("-------------------------------------------------------------------")

# Q2) Write a while loop which prints "Hello," plus each name in the list. i.e. "Hello sam."

li2 = ["sam", "lisa", "dave", "tom","john", "alex"]
update_list = []
i = 0

while i<len(li2):
    hello = f"Hello {li2[i]}"
    update_list.append(hello)
    i += 1
print(update_list)

print("-------------------------------------------------------------------")


# Q3) Print the greater than 5 numbers.

list1=[1,20,3,7,28,9,4]

i = 0

while i  < len(list1):
    if(list1[i]>5):
        print(f"{list1[i]} is greater than 5")
    i += 1

print("---------------------------------------------------------")

# Q4) Add square of each number from the given list.

# my_list = [3, 5, 6, 8, 4]
# Output:  [3,5,6,8,4,9,25,36,64,16]

# Solution ==> 

my_list = [3, 5, 6, 8, 4]
n = len(my_list)
i = 0

while i < n:
    sum1 = my_list[i] ** 2
    my_list.append(sum1)
    i += 1

print(my_list)


print("-------------------------------------------------------------------------------------------------")

# Q5)Write a Python program which iterates the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". (While LOOP)

# inp = int(input("Enter Number: "))

i = 1

while i <= 100:
    if(i % 3 == 0 and i % 5 == 0):
        print(f"FizzBuzz")
    elif(i % 3 == 0):
        print(f"Fizz")
    elif(i % 5 == 0):
        print(f"Buzz")
    else:
        print(i)
    i += 1

print("-------------------------------------------------------------------------------")

# Q7)Write a  program
# am to find the factors of numbers. (WHILE LOOP)
# Var num1 = 12;
# The factors of 12 is:
# 1  2  3  4  6  12

# Solution ==> 

fact_num = 10
i = 1

print(f"The factors for {fact_num}  are:")

while i <= fact_num:
    if(fact_num % i == 0):
        print(i)
    i += 1
    
