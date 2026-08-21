# 1
num1 = "10"
num2 = "20"
sum = int(num1) + int(num2)
print(sum)

# 2
str1 = "A blue bottle with blue liquid is on blue table red red red"

n_str = str1.replace("blue", 'temp')
n_str = n_str.replace('red', 'blue')
n_str = n_str.replace('temp', 'red')
print(n_str)

# 3
tuple1 = (11, 22, 44,55)
lis = list(tuple1)

lis[1] = 222
print(lis)

# 4
li3 = ["one","two",3,["four","five",45,23,["three","hello",34,"python"],"Eight",10],["seven",2],9,"six"]

print(li3[2])
print(li3[6])
print(li3[3][1])
print(li3[3][4][3][1:4])

# 5
y = [[["john","tom","taylor","kat","alex"]]]
print(y[0][0])

# 6
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 

list1[2][2].append(7000)
print(list1)

# 7
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

list1[2][1][2].extend(['h','i','j'])
print(list1)

# 8
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if a == b == c:
#     print("Equilateral triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle")
# else:
# print("Scalene triangle")

# 9

# n = int(input("Enter Number: "))
# l_d = n % 10
# if(l_d%3 == 0):
#     print("Divisible")
# else:
#     print("Not divisible")

# 10

# n1 = int(input("Enter Num1: "))
# n2 = int(input("Enter Num2: "))
# n3 = int(input("Enter Num3: "))

# s_l = 0


# if(n1>=n2 and n1<=n3) or (n1<=n2 and n1>= n3):
#     s_l = n1
#     print(f"Second Largest Number is {s_l}")
# elif(n2>=n1 and n2<=n3) or (n2<=n1 and n2>=n3):
#     s_l = n2
#     print(f"Second Largest Number is {s_l}")
# else:
#     s_l = n3
#     print(f"Second Largest Number is {s_l}")

# # 
# numbers = []

# for i in range(1,4):
#     num = int(input(f"Enter number {i}: "))
#     numbers.append(num)

# numbers.sort()

# print("Second largest number =", numbers[-2])

# n = []
# for i in range(10):
#     np = input(f"Enter Number {i+1}: ")
#     n.append(np)

a = 'Python'
print(a[0])

x = [1,3,54,32,56,17,24]

even = [i if i % 2 != 0 else i*i for i in x]
print(even)

print("Present" if 42 in x else "not present")
