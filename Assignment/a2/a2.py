"""
Q1. Write a program to swap the words "blue" and "red" in the string, so that every occurrence of "blue" becomes "red" and every occurrence of "red" becomes "blue".

str1 = "A blue bottle with blue liquid is on blue table red red red"

Q2) Write a python  program to modify the Second item (22) of a tuple.
Given :-  tuple1 = (11,22, 44, 55)
Expected output:
tuple1= (11, 222, 44, 55)
"""

# ------------------------------------------------------------------------------
# Q1 solution

a = "A blue bottle with blue liquid is on blue table red red red"
b = a.replace('blue','temp').replace('red','blue').replace('temp','red').capitalize()
print(b)


# -------------------------------------------------------------------------------
# Q2 solution

tuple1 = (11,22,33,44)
my_List = list(tuple1)
my_List[1] = 222
print(my_List)   # [11, 222, 33, 44]
