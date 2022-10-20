import sqlite3
from faker import Faker

# Get data from faker
faker = Faker()
names = [faker.name().split() for _ in range(1000)]
names = [name for name in names if len(name) == 2]

##Create table in data.db
#connection = sqlite3.connect('data.db')
# table = 'CREATE TABLE users (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)'
# cursor = connection.cursor()
# cursor.execute(table)
# connection.commit()

##Insert data into table
connection = sqlite3.connect('test.db')
insert_query = 'INSERT INTO users (FIRST_NAME, last_name) VALUES (?, ?)'
cursor = connection.cursor()
for name in names:
    cursor.execute(insert_query, name)
connection.commit()

##Select data from table
select_query = 'SELECT * FROM users LIMIT 10'
for i in cursor.execute(select_query):
    print(i)