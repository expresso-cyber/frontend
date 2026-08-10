# changing the value of the tuple by constructing a new list

t1 = ("hello", 33, 56, 77,98)

# here we are creating a new list from a tuple using list function ( Which is a built in function in a python.)

l1 = list(t1)

print(t1)  # printing tuple (t1) values
print(type(t1))  # printing data-type of tuple (t1)

print(l1) # printing list values
print(type(l1)) # printing the data-type of the list (l1)

print(len(t1)) # printing the length of tuple t1
print(len(l1)) # printing the length of list l1

print((len(l1) - 1))  # printing the index length of list (l1)
print(l1[len(l1) - 1]) # printing the last item of the list