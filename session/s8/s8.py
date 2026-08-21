n = 8
i = 1
while i<=n:
    if i % 2 == 0:
        i += 1
        continue
    j = 1
    while j<=10:
        print(i * j)
        j += 1
    i += 1

# User defined function

'''
def fun1():                 # Function declaration
    print('Hello Dev')

fun1()          # Call to function
'''

# Parameters and arguments

"""
def add(a,b):       #  Parameters
    print(a + b)

'''
# add(10,4)          # arguments
num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
# add(num1,num2)
'''
#add(10,5)
"""
'''
def hisghestNum(a,b,c):
    if c < a > b:
        print(a)
    elif c < b >  a:
        print(b)
    else:
        print(c)

num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
num3 = int(input('Num3: '))
# hisghestNum(num1,num2,num3)
'''
'''
num_1 = int(input('Num: '))
def evenNum(num):
    for i in range(1,num + 1):
        if i % 2 == 0:
            print(i)
evenNum(num_1)
'''

# global and local variable

'''
a = 10              # global
def fun():
    global a
    #a = 20             # local
    a += 2
    print(a)

fun()
print(a)
'''
# default parameters
'''
def add(a,b = 3):
    print(a + b)
#add()
add(10)
#add(10,40)
'''
#  *args
'''
def fun2(b,*a):
    s = 0
    for i in a:
        s += i
    print(s)
fun2(30,4,6,2)
fun2(30,4,6,2,54,123,3,54,23)
'''
#  **kwargs
def fun3(*a,**m):
    print(m)
    print(a)

fun3(30,20,name = 'Dev',age = 34)