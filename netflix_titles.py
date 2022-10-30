#!/usr/bin/env python3

## Import required modules
import csv
import sqlite3

## Connecting to the netflix_titles database
connection = sqlite3.connect('netflix_titles.db')

## Creating a cursor object to execute SQL queries on the netflix_titles database
cursor = connection.cursor()

## Defining table schema for the table, nfxtitle
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


## Creating the table into the netflix_titles database
# cursor.execute(create_table)

## Opening the netflix_titles.csv
file = open(
    'Netflix_datasets/netflix_titles.csv')

## Reading the contents of netflix_titles.csv
contents = csv.reader(file)

## SQL query to insert data into the nfxtitle table
# insert_records = "INSERT INTO nfxtitle (show_id, type, title, director,cast,country,date_added,release_year,rating,duration,listed_in,description) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

## Importing the contents of the csv file into nfxtitle table
# cursor.executemany(insert_records, contents)

## SQL queries to retrieve specified data from the nfxtitle table
### Query 1: Find Netflix Original Films with an IMDB Score Greater than 8.5
query1 = """SELECT Distinct country, count(title) 
		   FROM nfxtitle
		   WHERE country != ''
		   Group by country
		   Order by count(title) DESC
		   LIMIT 10;"""
top10_production_country = cursor.execute(query1).fetchall()
### Query 2: Find the top five genre with the highest IMDB Score from Netflix Original Movies
query2 = """SELECT Distinct type, release_year, count(title)
		   FROM nfxtitle
		   WHERE release_year != '' 
		   AND release_year in ('2021', '2020', '2019', '2018', '2017', '2016', '2015','2014','2013','2012')
		   Group by release_year
		   Order by release_year DESC;"""
top10_release_year = cursor.execute(query2).fetchall()

## Output to the console screen
###FROM Query 1
print('#'* 50)
print(f"BELOW ARE THE TOP 10 PRODUCTION COUNTRIES WITH THE MOST NETFLIX CONTENTS:")
for i in top10_production_country:
    print(i)
###FROM Query 2
print('#'* 50)
print(f"SHOW TYPE AND COUNT BREAK DOWN BY YEAR BETWEEN 2012 TO 2021:")
for j in top10_release_year:
	print(j)

## Committing the changes
connection.commit()

## closing the database connection
connection.close()
