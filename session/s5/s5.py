# loops

# Repetition of something
# Types of loops ==>
# a. While loop
# b. for loop


# a) while loop
# a. Initialize
# b. Condition
# c. Iteration

i = 1    # Initialize
while i <= 10:     # Condition
    print(f"{i}")
    i += 1         # Iteration


# Print the table of 25 till 250 times

y = 1
while y <= 10:
    print(f"25 * {y} = {25 * y}")
    y += 1


# Print the even numbers from 1-50
ne = input("Enter number: ")
n = 1

while n <= int(ne):
    if (n % 2 == 0):
        print(f"{n}")
    n += 1


# Print sum of N natural numbers.

# q = 10
# sum = 0
# i = 1

# while i <= q:
# sum += i
# i += 1


# print multiplication of the sum of N natural numbers

N = 10

sum = 1
i = 1

while i <= 10:
    sum *= i
    print(f"{sum} ||")
    i += 1

print(sum)


# Sum of elements of list

li = [22,44,33,45,76]

sum = 0
i = 0

while i<len(li):
    sum += li[i]
    i += 1
    
print(f"Sum of elements of the given list is: {sum}")


# Find the odd numbers in the list

li1 = [23,44,56,76,67,99,88]
count = 0
i = 0

while i < len(li1):
    if (not(li1[i] % 2 == 0)):  # or if(li1[i] % 2 != 0):
        print(f"{i}) {li1[i]}")
    i += 1


# Largest in the list

li2 = [99,55,898,95,67]

i = 0
max = li2[0]

while i < len(li2):
    if(li2[i] >= max):
        max = li2[i]
    i += 1

print(f"Maximum in the list is - {max}")


# print the letters of a string

string = "my name is roshan".strip().title()
i = 0

while i < len(string):
    print(f"Letter {i} is {string[i]}")
    i += 1

# count the number of words and characters present in the string

string1 = input("Enter string: ").strip()

string1 = input("Enter string: ")

i = 0
word = 0
char = 0
in_word = False

while i < len(string1):
    if string1[i] != " ":
        char += 1
        if in_word == False:
            word += 1
            in_word = True
    else:
        in_word = False
    i += 1

print("Words:", word)
print("Characters:", char)

# if string1 == "":
#     word = 0
#     char = 0
# else:
#     i = 0
#     word = 1
#     char = 0

#     while i < len(string1):
#         if string1[i] != " ":
#             char += 1
#         else:
#             word += 1
#         i += 1

# print("Words:", word)
# print("Characters:", char)

# string1 = "hello    dev".strip()
# i = 0
# word = 1
# char = 0

# while i < len(string1):
#     if(string1[i] == " "):
#         word = word + 1
#     else:
#         char = char + 1
#     i += 1

# print(word)
# print(char)

