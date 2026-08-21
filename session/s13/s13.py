# import json

"""
a = '[{"name":"Dev"}]'
print(a[0])
b = json.loads(a)
print(b[0])
"""
"""
a = [{"name":"Dev"}]
b = json.dumps(a)
print(b[0])
"""


# Web scrapping

# from bs4 import BeautifulSoup
# import requests

# url = "https://www.nike.in/men/men-s-shoes/c/92564?root=nav_3&ptype=listing%2Cmen%2Cshoes%2C1%2Call-shoes"
# data = requests.get(url)
# plain_text = data.text
# print(type(plain_text))

# res = BeautifulSoup(plain_text, "html.parser")
# print(type(res))

# title = res.find_all("div", {"class": "css-12xgt1"})
# print(title)
"""
for i in title:
    print(i.text)
    print('-' * 50

"""

# f = open("demo.txt", "w")
# k = 1
# for i in title:
#     f.write(f"{k}.{i.text}\n")
#     k += 1

# f.close()

"""
price = res.find_all('h3',{'class':'css-1a142u8'})

for i in price:
    k = i.text.replace('₹','').replace(',','')
    if float(k)>=17000 and float(k)<=20000:
        print(i.text)
        print('-' * 50)
"""
