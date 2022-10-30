#!/usr/bin/env python3

## Prep: Import required modules
from sqlalchemy import create_engine
import pandas as pd

# Step 1: Create a dataframe from the csv file
netflix_mv_ratings = pd.read_csv('Netflix_datasets/netflix_movie_rating.csv', encoding='latin')

# Step 2: Create a reference for sql library
engine = create_engine('sqlite://',echo = False)
 
# Step 3: Attach the data frame to the sql library and name the table as "mv_ratings"
netflix_mv_ratings.to_sql('mv_ratings',con = engine)

# Step 4: Query the sql table
## Query 1: Find Netflix Original Films with an IMDB Score Greater than 8.5. 
query1 = """SELECT Title, Genre, IMDB_Score
           FROM mv_ratings
           WHERE IMDB_Score > 8.5
           ORDER BY IMDB_Score DESC
           """
greater_than_8 = engine.execute(query1).fetchall()
## Query 2: Find the highest IMDb scores of the top 5 genre for Netflix Original Movies
query2 = """SELECT DISTINCT Genre, max(IMDB_Score)
           FROM mv_ratings
           GROUP BY Genre
           ORDER BY IMDB_Score DESC
           LIMIT 5;
          """
highest_rating_genre = engine.execute(query2).fetchall()

# Step 5: Output to the console screen
##From Query 1
print('#'* 50)
print(f"Netflix Original Films with an IMDB Score Greater than 8.5:")
for i in greater_than_8:
	print(i)
##From Query 2
print('#'* 50)
print(f"The Top Five Netflix Original Movie Genres and their Respective IMDb Scores:")
for j in highest_rating_genre:
	print(j)