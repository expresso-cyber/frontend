li = [23,56,77,88]
n = len(li)

i = 0

while i < n:
    print(f"{li[i]}")
    i += 1

print("----------")

# print 10-1 using for loop

for i in range(1,11)[1:]:  # or range(10,0,-1)
    print(i)
    

print("----------------------------")


for i in range(1,6):
    print(f"{i},{i+3}")


print("------------------------------")

# Take two input as a starting and ending value then do sum of all the even between between those numbers

v1 = int(input("Enter number : "))
v2 = int(input("Enter number : "))

sum = 0

for i in range(v1,v2):
    if(i % 2 == 0):
        sum += i

print(sum)


print("-----------------------------------")

# Reverse the List

li = [22,13,55,76]

li2 = []

for i in range(len(li))[::-1]:
    li2.append(li[i])
    
print(li2)


# or Second method without using range function()

# print(f"Reverse of the given list is {li3}")



print("--------------------------------------------------------")

# to check or find whether the value is present in the collection 


rollNoList = [34,55,76,55]

isPresent = False
val = 34
if val in rollNoList:
    isPresent  = True
    print(isPresent)
else:
    print(isPresent)


print("-------------------------------------")


# Print the first and last index of number 3 from the given list

li4 = [1,3,5,6,8,34,66,3,3,56,3]

n_l = []

for i in range(len(li4)):
    if li4[i] == 3:  # or if 3 in li4
        n_l.append(i)   # append index of every 3 in the new list
        
print(n_l)
print(f"{n_l[0]}  {n_l[-1]}")


print("---------------------------------------")

# li5 = [122,34,55,23,78]

# l = li1[0]
# s_l = li1[0]

# for i in range(len[li])
