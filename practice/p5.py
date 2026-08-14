print(bool("Hey"))
print(float("123.45"))


# What is the printed output of x = 5; print("Yes" if x > 3 else "No")?
x = 5
print("Yes" if x > 3 else "NO")


print(True if 0.1 + 0.2 == 0.3 else False)
print(0.1+0.2)

print(bool([]))


# What is the output of for x in "CS": print(x, end="")?
for x in "CS":
    print(x, end=" ")
    print()


# What is the final value of s after executing s = 0; for i in range(4): s += i?
s = 0
for i in range(4):
    s += i
    print(f"{s} + {i} => {s}")

print(s)

# What is the output of i = 1; while i < 4: print(i, end=" "); i += 2?

i = 1
while i<4:
    print(i, end=" ")  # 1 3
    i += 2

print()


a = 5
b = "5"
print(a == b)
print(a == int(b))

x = 10
x = 'ten'
print(x)
print(type(x))

li = [1,2,3,34,"hey",True]

li.append("hii")
li.insert(5,"fourth")
li.extend(["my", 34,False])
print(li)

a = li.pop(5)
print(a)

b = li.remove("hii")
print(b)
print(li)

# li.clear()
# print(li)

# li.reverse()
# print(li)

print(li.index(34))
print(li.count(34))
k = li.copy()
print(k)

del k
# print(k)

# Sets

s = {"hey",34, False, True}

print(s)

s.add(38)
s.update([34,"hii"])
print(s.pop())
print(s)

li2 = [2,3,4,98,76,]
t = tuple(li2)
print(t)
print(max(li2))
