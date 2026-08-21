from mymodule import hi_msg as hm
# import time
from time import sleep

# import re
# print(type(time))
# print(dir(time))

# a = time.localtime()
# time_dict = {13:1,14:2}
# print(f"{time_dict[a[3]}]:{a[4]}:{a[5]}")

# print('Hello')
# time.sleep(5)
# print('Dev')
"""
cp ='dev@gmail.com'
i = 1
while True:
    msg = input('Enter your password: ')

    if msg == cp:
        print('Hey , Welcome!!!')
        break
    elif i == 3:
        print('Sleep mode...')
        sleep(5)
        i = 1
    elif msg != cp:
        print('Try again...')
        i += 1
"""

"""
pwd = input('Enter your password: ')
flag = True
while flag:
    if len(pwd) <= 8 or len(pwd) >= 16:
        break
    elif not(re.search('[A-Z]',pwd)):
        break
    elif not(re.search('[a-z]',pwd)):
        break
    elif not(re.search('[0-9]',pwd)):
        break
    elif not(re.search('[@#$%^&*]',pwd)):
        break
    else:
        print('Valid password!!!')
        flag = False
if flag:
    print('Invalid password!!!') 
"""

# User defined modules
"""
import mymodule
#print(type(mymodule))
#print(dir(mymodule))
mymodule.hello_msg('Dev')
mymodule.hi_msg('Dev')
"""

# from mymodule import hi_msg,hello_msg
# from mymodule import *
# hi_msg('Dev')
# hello_msg('Python')

# import mymodule as mm
# mm.hi_msg('Python')


hm("Dev")
