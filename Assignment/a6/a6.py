# Q1) Write a python program to Find missing value.

Li = [2, 7]

m_val = []

for val in range(Li[0],Li[-1]):
    if val not in Li:
        m_val.append(val)

print(f"Missing Values are: {m_val}")

print("------------------------------------------------------------")

# Q2) Write a Python program to find and print the highest and lowest numbers from a given list of integers.

numbers = [23, 5, 89, 12, 45, 1, 67, 34, 90, 8]

i = 0
maximum = numbers[0]
minimum = numbers[0]

for i in range(len(numbers)):
    if(numbers[i] > maximum):
        maximum = numbers[i]
    if(numbers[i] < minimum):
        # print(f"{numbers[i]} is smaller than {minimum}")   # For understanding the code
        minimum = numbers[i]


print(f"Largest number: {maximum}, Smallest Number: {minimum}")


print("------------------------------------------------------------------")

# Q3) Write a Python program to move all 0 values in a list to the end while maintaining the relative order of the non-zero elements.

li1 = [0, 0, 1, 2,5,0,7,5,0,0,3,-3,0,-45]

for i in range(len(li1)):
    if(li1[i] == 0):
        li1.append(li1[i])
        li1.remove(li1[i])

print(li1)

print("------------------------------------------------------------------------------------")

# Q4) Write a python program ,to find the first and last indices(index) of the number (3) in the list?

li2 = [2, 3, 4, 5, 6, 3, 9, 10, 3, 92, 3, 5, 3, 66, 3, 22, 3, 45, 3]
new_l = []

for i in range(len(li2)):
    if (li2[i] == 3):
        new_l.append(i)

print(f"First Index: {new_l[0]} , Second Index: {new_l[-1]}")

print("----------------------------------------------------------------------")


# Q5) Write a python program to print second largest element from the given list

Li2 = [26, 48, 3, 1, 67, 83, 9, 23]

largest = Li2[0]
second_largest = Li2[0]

for i in range(len(Li2)):
    if Li2[i] > largest:
        second_largest = largest
        largest = Li2[i]
    elif Li2[i] > second_largest and Li2[i] != largest:
        second_largest = Li2[i]

print("Second largest element is:", second_largest)


print("----------------------------------------------------------------------")

# Q6) Write a Python program to count the number of vowels in a string using a for loop

v = "Hey my name is Rahul. And I am a programmAer".strip().lower()
count = 0

for i in range(len(v)):
    if(v[i] == 'a' or v[i] =='e' or v[i] == 'i' or v[i] == 'o' or v[i] == 'u'):
        # print(f"{i} ==> {v[i]}")
        count += 1


print(f"Number of vowels in this string is: {count}")

print("--------------------------------------------------------------------------")


# Q7) Write a Python program to reverse a string using a for loop.

str1 = "How are you"
str2 = ""

for ch in str1:
    str2 = ch + str2

print(f"Reverse of the given string is: {str2}")

print("------------------------------------------------------------------------------")


# Q8)Python program to determine whether the given number is a Harshad Number.(user input)What is Harshad number?
# (A number is said to be the Harshad number if it is divisible by the sum of its digit.
# For example, if number is 156, then sum of its digit will be 1 + 5 + 6 = 12. Since 156 is divisible by 12. So, 156 is a Harshad number.)

num = int(input("Enter a number: "))

sum_digits = 0
temp = num

for digit in str(temp):
    sum_digits = sum_digits + int(digit)

if num % sum_digits == 0:
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")
