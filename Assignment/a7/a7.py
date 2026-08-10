# Q1) Write a PYTHON program to print the multiplication tables of all ODD numbers up to a given integer n. Use a While loop and include either the break or continue statement

num = int(input("Enter Number: "))

i = 1

while i<=num:
    if(i % 2 == 0):
        i += 1
        continue
    
    print(f"Table of {i}:")
    
    j = 1
    
    while j <= 10:
        print(f"{i} * {j} = {i * j}")
        j += 1
        
    i += 1

