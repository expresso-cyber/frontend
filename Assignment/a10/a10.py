import pandas as pd
from pathlib import Path

# Q 1  Print all data of  director "Ridley Scott".

csv_file = Path(__file__).parent / "./IMDB-MovieData.csv"

data = pd.read_csv(csv_file)
ridley_scott = (data["Director"] == "Ridley Scott")

print(data[ridley_scott])


# Q2)  Print  all data of  "Ridley Scott" movies which ratings are greataer than 5 .

rating = data["Rating"] > 5
res = data[(ridley_scott) & (rating)]
print(res)

# Q3 ) Print movies from 2005 to 2010 which ratings are above 8.

rate = data["Rating"] > 8
movies = data[(data["Year"] >= 2005) & (data["Year"] <= 2010) & (rate)]
print(movies)

#  Q4) Create new column name "rating_catogory" and check whether ratings are above 8 then print "good" else "bad" in "rating_catogory".

data["rating-category"] = data["Rating"].apply(lambda x: "good" if x>8 else "bad")
print(data)