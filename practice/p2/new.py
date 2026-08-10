# 1. Write a program that declares four variables of type str, int, float and bool, then prints each value along with its type using the type() function.

# solution =>
str1 = "Hello"
print(str1)
print(type(str1))

num = 34
print(num)
print(type(num))

dec = 22.3
print(dec)
print(type(dec))

boolean = True
print(boolean)
print(type(boolean))


# 2. Write a program that stores your first name, last name and age in separate variables and prints a sentence such as 'My name is <first> <last> and age is <age>' using string concatenation with the '+' operator (remember to type-cast the age).

# Solution =>
fName, lName = "Roshan", "Rai"
age = 22
age2 = str(age)


print("My name is " + fName + " " + lName + " and age is " + age2)

#  Q3. Write a program that stores the numbers '15' and '25' as strings, converts both to integers using int(), adds them, and prints the result along with the type of the result.

num1 = "15" 
num2 = "25" 

total = int(num1) + int(num2)

print(total)
print(type(total))

# Q4 Write a program that takes a string as input from the user using input(), then prints its first character, its last character (using negative indexing) and its total length using len().

# Solution =>

# str3 = input("Enter your first name: ").strip()

# if len(str3) == 0:
#     print("You Entered Nothing. ")
# else:
#     print(str3[0])
#     print(str3[-1])
#     print(len(str3))


# Q5. Given the string m = 'We are learning Python', write statements using slicing to print: (a) the first 6 characters, (b) the last 6 characters, (c) the string reversed

m = "We are learning Java"

print(m[:6])
print(m[-6:])
print(m[::-1])

# Q6. Create a list li1 = ['Dev', 12, 34, 'Python', 23.45]. Print the list, its type, its length, the elements from index 2 onward, and the list in reverse order using slicing.

li1 = ["Dev", 12, 34, "Python", 23.45]

print(li1)
print(type(li1))
print(len(li1))
print(li1[2:])
print(li1[::-1])

# Q6 Write a program that takes the string ' hello Dev ' and prints: the stripped & capitalized version, the title-cased version, and the upper-case version, using appropriate string methods.


n = " hello Dev "

print(n.strip().capitalize())
print(n.strip().title())
print(n.strip().upper())
print(n.strip().index('v'))

# Q7 Write a program that uses an f-string to print 'My name is <name> and age is <age>.' Then create a tuple t1 = ('Dev', 12, 34, 'Python', 23.45) and print the tuple, its type and its length.

nam = "Roshan"
a = 22

print(f"My name is {nam} and age is {a}")

t1 = ('Dev',12, 34, 'Python', 23.45)
print(t1)
print(type(t1))
print(len(t1))