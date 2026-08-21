"""
li1 = []
for i in range(1,101):
    li1.append(i)
print(li1)
"""

# List comprehension
"""
#li1 = [(i) for i in range(1,101)]
#print(li1)

li2 = list(range(1,101))
print(li2)
"""

# ternary operator
# age = 32
# res = "You can vote" if age >= 18  else "You can't vote"
# print(res)
"""

num = int(input('Num1: '))

if num % 2 == 0:
    if num > 0:
        print('num is even and +ve')
    else:
        print('num is even and -ve')
else:
    if num > 0:
        print('num is Odd and +ve')
    else:
        print('num is Odd and -ve')
"""
# ans = ('E & P' if num>0 else 'E and N') if num % 2 == 0 else ('O & P' if num>0 else 'O and N')
# print(ans)

"""
li1 =  [3,5,6,2,7,8,9]
li2 = [(i if i % 2 == 0 else i ** 2) for i in li1]
print(li2)
"""

# lambda function / anonymous function
"""
def fun():
    print('Hello')

fun()
"""

"""
a = lambda name: f"Hello {name}"
print(a('Dev'))
"""


# map & filter
# li1 =  [3,35,62,2,72,18,9]
# filter
# def showRes(m):
# if m >= 20:
#    return m
# return m>=20

# li2 = list(filter(showRes,li1))
# li2 = list(filter(lambda n:n>=20,li1))
# print(li2)

# map
"""
def showRes(a):
    #if a >= 20:
    #    return a
    #else:
    #    return a**2
    return a ** 2

li2 = list(map(showRes,li1))
"""
# li2 = list(map(lambda b : b ** 2,li1))
# li2 = list(map(lambda b : b ** 2 if b % 2 == 0 else b,li1))
# print(li2)


li1 = [3, 35, 62, 2, 72, 18, 9]
"""
a = list(filter(lambda a : a>=20,li1))
b = list(map(lambda m:m**2,a))
"""

b = list(map(lambda m: m**2, filter(lambda a: a >= 20, li1)))
print(b)
