'''
a = 24
num = a

sum1 = 0    # 6
while a > 0:
    b = a % 10      # 3  1  2
    sum1 += b       
    a //= 10

if num % sum1 == 0:
    print('Harshad')
else:
    print('not')
'''


#  break and continue
'''
str1 = 'Javascript'
for i in str1:
    if i == 's':
        #break
        continue
    print(i)
'''
'''
num = int(input('Num: '))
i = 1
while i <= num:
    if i % 5 == 0:
        print('Sorry')
        break
    print(i ** 2)
    i += 1
'''
'''
num = int(input('Num: '))  # 12
i = 1
while i <= num:
    if i % 5 == 0:
        print('Sorry')
        i += 1
        continue
    print(i ** 2)
    i += 1
'''
'''
num = int(input('Num: '))  # 12
i = 0
while i < num:
    i += 1
    if i % 5 == 0:
        print('Sorry')
        continue
    print(i ** 2)
'''
'''
num = int(input('Num: '))
for i in range(1,num + 1):
    if i % 5 == 0:
        print('Sorry')
        continue
    print(i ** 2)
'''
'''
i = 1
while True:
    if i == 11:
        break
    print(i)
    i += 1
'''

while True:
    num1 = int(input('num1 : '))
    num2 = int(input('num2 : '))
    op = input('Please select your operator (+,-,*,/): ')

    if op == '+':
        print(f"{num1} {op} {num2} = {num1 + num2}")    
    elif op == '-':
        print(f"{num1} {op} {num2} = {num1 - num2}")
    elif op == '*':
        print(f"{num1} {op} {num2} = {num1 * num2}")
    elif op == '/':
        print(f"{num1} {op} {num2} = {num1 / num2}")    
    else:
        print('Invalid operator!!!')


    msg = input('Do you want to continue PRESS y or PRESS any Key to STOP: ').lower()
    if msg != 'y':
        print('Game over!!!')
        break
