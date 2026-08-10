# Q1) Write a Python function that checks whether a passed string is palindrome or not.

# Solution ==>
def isPalindrome(str):
    # Writing logic for reversing the string and then comparing it with the original string

    rev = ""

    for ch in str:
        rev = ch + rev
    print(f"Reverse of the given string is : {rev}")

    if(str == rev):
        print("Palindrome")
    else:
        print("Not a Palindrome.")

    # using string slicing to reverse the string and then comparing with the original string.
    # if(str == str[::-1]):
    #     print("palindrome")
    # else:
    #     print("Not palindrome")

isPalindrome("hello")


print("--------------------------------------------------------------------------------")

# Q2) Find Factors of Number

def factorOfNum(num):
    i = 1
    while num >= i:
        if(num % i == 0):
            print(i)
        i += 1

factorOfNum(24)

print("--------------------------------------------------------------------------------")

# Q3) Write a function to Check whether a given year is a leap year or not

# 2016
# 1896
# 1900
# 1904

def isLeap(y):
    if(y % 4 == 0):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")
        
year = int(input("Enter year: "))
isLeap(year)
