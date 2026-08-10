# a = 'red red hello blue blue'
# b = a.replace('red','temp').replace('blue','red').replace('temp','blue')
# b = a.replace('red','BLUE').replace('blue','RED').capitalize()
# print(b)


"""
ti1  = (10,20,40,5)
li1 = list(ti1)
li1[1] = 200
ti1 = tuple(li1)
print(ti1)
"""

# Nested List

# li1 = [10,20,[30,40,[60,70],90,[12,45,[6,67],17]],12,[23,[55,[5,7]]]]
# print(len(li1))

# print(li1[1])
# print(li1[2][1])
# print(li1[4][1][0])
# print(li1[2][2][0])
# print(li1[-1][-1][-1][-1])
# print(li1[2][-1][-1])
# print(li1[2][-1][2][1])


# List methods
# li1 = [10,20,30,40,50]
# li1.append(60)
# li1.insert(1,60)
# li1.pop()
# a = li1.pop(2)
# print(a)
# li1.remove(20)
# li1.clear()
# li1.reverse()
# print(li1[::-1])
# del li1[3]
# li1.extend([60,70,34,534,])
# print(li1)

# a = li1.index(30)
# a = li1.count(30)
# a = li1.copy()
# print(a)

# a = []
# f_name = input('First name: ')
# l_name = input('Last name: ')
# a.extend([f_name,l_name])
# a.append(f_name)
# a.insert(1,l_name)
# print(a)

"""
a = [10,20,30]
b = a
b.append(40)
print(a)
print(b)
"""
"""
a = [10,20,30]
c = a.copy()
c.append(40)
print(a)
print(c)

"""

# 3.set    {}     Mutable

# s1 = {10,20,30,10,'Dev',40,'Dev',"Python",70}
# print(s1)
# print(type(s1))
# print(len(s1))


# set methods

# s2= {20,4,5,'Dev',"Python",34,6}
# s2.add(45)
# s2.update({45,523})
# s2.update([45,523])
# s2.update((45,523))
# s2.pop()
# s2.remove(4)
# s2.remove(14)
# s2.discard(4)
# s2.discard(14)
# s2.clear()
# del s2
# print(s2)
# a = s2.copy()
# print(a)


# 4.dict   {}   key : value pair  (mutable)
# di1 = {'name':'Devesh','age':34,'email':'dev@gmail.com','name':'Dev'}
# print(di1)
# print(type(di1))
# print(len(di1))
# print(di1['email'])
# di1['age'] = 35
# inp1  = input('Hobby: ')
# di1['hobby'] = inp1
# print(di1)
"""
di2 = [
  {
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
    "rating": {
      "rate": 3.9,
      "count": 120
    }
  },
  {
    "id": 2,
    "title": "Mens Casual Premium Slim Fit T-Shirts ",
    "price": 22.3,
    "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
    "rating": {
      "rate": [4.1,4.4],
      "count": 259
    }
  }]
"""
# print(di2[0]['title'])
# print(di2[1]['rating']['rate'][1])
# di2[1]['rating']['count'] = 300
# print(di2[1])


# dict methods

di1 = {"name": "Dev", "age": 34}
# di1.update({'email':'Dev@','contact':[723,971269]})
# di1.popitem()
# di1.pop('name')
# di1.clear()
# del di1['name']
# print(di1)

# a = di1.copy()
# a = di1.items()
# a = di1.keys()
# a = di1.values()
# print(a)
