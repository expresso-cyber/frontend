# ---------------------------------------------------------------------
# Q1 Solution

li3 = ["one","two",3,["four", "five", 45, 23, ["three", "hello", 34, "python"], "Eight", 10],["seven", 2],9,"six"]

print(li3[2])       # 3
print(li3[-1])      # six
print(li3[3][1])    # five
print(li3[3][4][3][1:4])  # yth
print(li3[4][1])    # 2


# ------------------------------------------------------------------------------------------
# Q2 Solution

list1 = ["Name", ["John", 20, "tom", 10], "subject", ["Python", "PHP"]]

a = list1[0]
b = list1[1][0]
c = list1[1][1]
d = list1[2]
e = list1[3][0]

result = (f"{a} is {b} age is {c} and his {d} is {e}")
print(result)


# -------------------------------------------------------------
# Q3 Solution

y = [[["john", "tom", "taylor", "kat", "alex"]]]

y1 = y[0][0]
print(y1)


# ----------------------------------------------------------------
# Q4 Solution

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)


# ------------------------------------------------------------------
# Q5 Solution

list2 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

list2[2][1][2].extend(['h','i','j'])
print(list2)
