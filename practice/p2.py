# Q1. Write a program to swap the words "blue" and "red" in the string, so that every occurrence of "blue" becomes "red" and every occurrence of "red" becomes "blue".

str1 = "A blue bottle with blue liquid is on blue table red red red".strip().capitalize()

str2 = str1.replace("blue", "temp")
print(str2)
str2 = str2.replace("red", "blue")
print(str2)
str2 = str2.replace("temp","red")

print(str2)

# Q2) Write a python  program to modify the Second item (22) of a tuple.
# Given :-  tuple1 = (11,22, 44, 55)
# Expected output:
# tuple1= (11, 222, 44, 55)

tuple1 = (11, 22, 44, 55)

# First Converting tuple into list
li = list(tuple1)
li[1] = 222   # assigning the value 222 to the index 1

# then converting the list into tuple
tuple1 = tuple(li)

print(tuple1)
