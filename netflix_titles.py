# Import required modules
import csv
import sqlite3


# Connecting to the geeks database
connection = sqlite3.connect('netflix_titles.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

## Table Definition
# create_table = '''CREATE TABLE nfxtitle(
# 				show_id VAR PRIMARY KEY,
# 				type VAR,
# 				title VAR,
# 				director VAR,
# 				cast VAR,
# 				country VAR,
# 				date_added DATE,
# 				release_year DATE,
# 				rating VAR,
# 				duration VAR,
# 				listed_in VAR,
# 				description VAR
# 				);
# 				'''


# # Creating the table into our
# # database
# cursor.execute(create_table)

# Opening the person-records.csv file
file = open(
    'Netflix_datasets/netflix_titles.csv')

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)

# # SQL query to insert data into the
# # person table
# insert_records = "INSERT INTO nfxtitle (show_id, type, title, director,cast,country,date_added,release_year,rating,duration,listed_in,description) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# # Importing the contents of the file
# # into our person table
# cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
query1 = """SELECT Distinct country, count(title) 
		   FROM nfxtitle
		   WHERE country != ''
		   Group by country
		   Order by count(title) DESC
		   LIMIT 10;"""
query2 = """SELECT Distinct type, release_year, count(title)
		   FROM nfxtitle
		   WHERE release_year != '' 
		   AND release_year in ('2021', '2020', '2019', '2018', '2017', '2016', '2015','2014','2013','2012')
		   Group by release_year
		   Order by release_year DESC;"""

top10_production_country = cursor.execute(query1).fetchall()
top10_release_year = cursor.execute(query2).fetchall()

# Output to the console screen
print('#'* 50)
print(f"BELOW ARE THE TOP 10 PRODUCTION COUNTRIES WITH THE MOST NETFLIX CONTENTS:")
for i in top10_production_country:
    print(i)

print('#'* 50)
print(f"SHOW TYPE AND COUNT BREAK DOWN BY YEAR BETWEEN 2012 TO 2021:")
for j in top10_release_year:
	print(j)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()
