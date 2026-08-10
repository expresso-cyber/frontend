#  user input

#a = input('Enter your name: ')
#print("My name is "+a)

# String indexing and length

#a = 'Python'
#print(a[0])
#print(len(a))
'''
b = input('Enter your string: ').strip()
length = len(b)-1
print(b[length])
print(b[-1])
'''

# String slicing

#m = 'We are learning Python'
#print(m[0])
#print(m[3:6])
#print(m[3:])
#print(m[:6])
#print(m[-1])
#print(m[:-1])
#print(m[::1])
#print(m[::-1])
#print(m[-6:])
#print(m[:7]+m[-6:])
#print(m[-8:-16:-1])

# String Methods
'''
a = 'hello'.upper()
print(a)
b = 'HELLO'.lower()
print(b)
c = '   hello Dev    '
print(c.strip().capitalize())
d = 'hello Dev'.capitalize()
print(d)
e = 'hello Dev'.title()
print(e)
f = 'AAAHalloaaaa'
g = f.replace('a','e').lower()
print(g)

i = 'hello'
print(i.startswith('he'))
print(i.endswith('la'))
'''
#j =  'Hello'
#print(j.index('e'))
#print(j.count('d'))
'''
a,d = 10,'Dev'
print(a)
print(d)
'''
'''
# f string  ->  formetted string
a = 'Dev'
b = 34
print(f"My name is {a} and age is {b}.")
'''


# 2. Non - Primitive data types  (Mutable)
#a.list     []
#b.tuple    ()
#c.set      {}
#d.dict     {}


#a.list     []    mutable
'''
li1 = ['Dev',12,34,'Python',23.45]
print(li1)
print(type(li1))
print(len(li1))
'''

# list indexing / slicing

li2 = [10,20,40,50,60]

#print(li2[4])
#li2[1] = 200
#print(li2)

#print(li2[2:4])
print(li2[2:])
print(li2[:4])
print(li2[-1])
print(li2[:-1])
print(li2[::-1])

'''
t2= (10,20,40,50,60)
t2[1] = 200
print(t2)
'''



#b.tuple    ()     Immutable
'''
t1 = ('Dev',12,34,'Python',23.45)
print(t1)
print(type(t1))
print(len(t1))
'''