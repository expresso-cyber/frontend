# Q1) Factorial using recursion function
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

fact = factorial(4)
print(fact)

print("---------------------------------------------------")

# Q2)
def f(n):
    if n <= 1:
        return n

    return f(n - 1) + f(n - 2)

ip = int(input("Enter Number: "))
li = []
for i in range(ip):
    a = f"{f(i)}"
    li.append(a)

print(li)