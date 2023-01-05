# Project-3-Heather-Qiu
[![GitHub Action for Continuous Integration](https://github.com/nogibjj/hq-individual_project3/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/hq-individual_project3/actions/workflows/main.yml)


## Project Description

The project is done for IDS 706 Data Engineering class at Duke University. The goal is to generate a script that queries a SQL database to drive insights. While flat files such as .csv files provide an excellent mechanism for storing data, relational databases allow one to express items and their relationships. In this project, we will explore two ways to build and query databases to extract useful information: SQLite and SQLAlchemy.

* SQLite is a self-contained and serverless single-file database engine. Check out [this post](https://www.w3schools.blog/sqlite-tutorial) from W3schools to learn more if you are interested. 

* SQLAlchemy is a third-party Python library that facilitates communication between Python programs and databases. SQLAlchemy supports many databases, such as SQLite, Postgresql, and MySQL. Check out [this post](https://medium.com/geekculture/getting-started-with-sqlalchemy-d132d04c940) from medium.com to learn more if you are interested.  


## Data Flow Diagram
![SQLAlchemy & SQLite](https://user-images.githubusercontent.com/105904149/198904778-5ed348a0-1c3d-408d-bdd2-1662ef5e8f62.png)


## Demo Video
[Project 3 - Heather Qiu - SQL in Python - Watch Video](https://youtu.be/m2qZnPyXZIQ)

Two Kaggle datasets are used in this demo:

* [Netflix Original Films & IMDB Scores](https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores): consists of all Netflix original films released as of June 1st, 2021. `netflix_mv_ratings.py` leverages SQLAlchemy to establish communication between the database, fed with data from the relative path `netflix_movie_rating.csv`, and Python programs. It then queries the database and returns results for (1) Netflix Original films with an IMDB Score Greater than 8.5 and (2) the top five Netflix Original Movie genres & their respective IMDb Scores.

* [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows): consists of over 8000 movies or tv shows available on Netflix as of mid 2021. `netflix_titles.py` uses SQLite3. The script is designed to create a connection, insert data, and read into `netflix_titles.db`. The built-in SQL statements then fetch results for (1) the top ten production countries with the most Netlfix contents and (2) a breakdown of show type by year over ten years (2012 to 2021). 


## Instructions To Replicate the Process Yourself

To run the python scripts after cloning the repository, type in your terminal: `python <filename>.py`. An example is `python netflix_mv_ratings.py`, which returns results described in the demo section. Please note that to run `python netflix_titles.py` you need to uncomment steps 3 through 8 in the respective file to build the database local to your machine.
