# import
# import requests

"""
url = 'https://fakestoreapi.com/products'
data = requests.get(url)
#print(data)

plain_text = data.text
#print(type(plain_text))

res = json.loads(plain_text)
#print(type(res))
#print(res[0]['title'])

for i in res:
    print(i['title'])

a = list(map(lambda a:a['title'],res))
print(a)
"""
"""
api_key = 'c4a374bc64a24d6189fecbad8302cb5d'
city_name = input('City name: ')
url  = f'https://api.weatherbit.io/v2.0/current?city={city_name}&key={api_key}'
res = json.loads(requests.get(url).text)
print(res['data'][0]['temp'])
"""

"""
Hello Dev
Hello Python
Hello World

"""
"""
mode
t    =>  binary
r    => read
w    =>  write
a    =>  append
r+   => read and write
"""
# file handling
f = open("demo.txt", "w")

# print(f.read())
# print(f.read())
# print(f.read(3))

# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.readlines())
# f.write('Hi')
li1 = ["a", "b", "c", "d"]
for i in li1:
    f.write(f"{i}\n")

f.close()
