"""
Q1) print  values

Given :-  li=["one","two",3,["four","five",45,23,["three","hello",34,"python"],"Eight",10],["seven",2],9,"six"]
expected output:
3
six
five
python => yth (Print yth)
2
"""
# Solution ==>
li = [
    "one",
    "two",
    3,
    ["four", "five", 45, 23, ["three", "hello", 34, "python"], "Eight", 10],
    ["seven", 2],
    9,
    "six",
]

print(li[2])
print(li[6])
print(li[3][1])
print(li[3][4][3][1:4])
print(li[4][1])


print("----------------------------------------------------------------")


# Q.s 2) Write a python program to print following output.
# Given :- list1 = ["Name",["John",20,"tom",10],"subject",["Python","PHP"]]
# expected output :
# Name is john age is 20 and his subject is Python

# Solution ==>
list1 = ["Name", ["John", 20, "tom", 10], "subject", ["Python", "PHP"]]

print(f"{list1[0]} is {list1[1][0]} age is {list1[1][1]} and his {list1[2]} is {list1[3][0]}")


print("-----------------------------------------------------")


# Q.s 3) Write a python program to print following output.
# Given :- y = [[["john","tom","taylor","kat","alex"]]]
# expected output :
# ['john', 'tom','taylor', 'kat', 'alex']

# Solution ==>
y = [[["john", "tom", "taylor", "kat", "alex"]]]

print(y[0][0])

print("------------------------------------------------------------")

""" 
Q4)Write a program to add item 7000 after 6000 in the following Python List 
Given :-  list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
Expected output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""

# Solution ==>

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].insert(3,7000)

print(list1)

print("------------------------------------------------------------")


"""
Q5)Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
Given :-  list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
expected output :
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
"""

l1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

l1[2][1][2].extend(["h","i","j"])

print(l1)