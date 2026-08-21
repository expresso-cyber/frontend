from pathlib import Path
import pandas as pd

# pip freeze

csv_file = Path(__file__).parent / "marks.csv"

data = pd.read_csv(csv_file)

print(data.head(2))
print("*" * 50)

print(data.tail(8))
print("-" * 50)

print(data.columns.values)
print()

# print(data[["Maths","Physics","Chemistry"]])
# print(data["Maths","Physics"])

data = data.fillna(0)
data = data.dropna()

data["Total"] = data["Physics"] + data["Maths"] + data["Chemistry"]
# print(data)

# def showRes(n):
# return "pass" if n > 200 else "fail"

data["Result"] = data["Total"].apply(lambda n: "pass" if n > 200 else "fail")

# print(data.duplicated())

# print(data.drop_duplicates())

print(data)

# data.to_csv("new.csv")

# steps
# import pandas as pd

# data = pd.read_csv('filename')

# data.head() prints the first 5 row of the csv data [Note: we can add the numbers of rows we want inside the bracket of head(here)]

# data.tail() prins the last 5 row of the csv data [Note: we can add the numbers of rows we want inside the bracket of head(here)]

# data.fillna()

# data.dropna() [Note: It remove the entire line]

# for printing the multiple column we want,  we can do like data["Total"] = data[["column1","column2, column3"]]

# for addition of different values from different columns ->  data["Result"] = data["column1"] + data["column2"] + data["column3"]

# for creating new column we could simply create a column name and inside it we can apply all the data we have created -> data["Result"] = data["Total"].apply(lambda n: "pass" if n > 200 else "fail")

# To store the changes in the file we have to create a new file, within that file we will create our new file using -> data.to_csv('filename'). Then all the data will be moved in this file.

# data = data.loc[2:6]   # this will print the exact rows from 2 to 6
# data = data.iloc[2:6] # this will print the rows from 2 to 5, it will not consider 6 becuase iloc[] works like slicing

# Instead of using iloc[] we could simple use data[2:6] -> this will work the same like iloc[]

# for getting the value through condition by iteration we can use the below thing:
# data = data.loc[(data["Maths"] > 30) & (data["Result"] == "fail")]  # use conditon inside the .loc((condition1) & (condition2)) or .loc(condition) or .loc((condition1) | (condition2))

# print(data.duplicated()) -> for finding the duplicates
# print(data.drop_duplicates()) -> for removing the duplicates
