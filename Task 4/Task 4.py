import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "admin"
)

print(db)

# creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

# creating a databse called 'datacamp'
# 'execute()' method is used to compile a 'SQL' statement
# below statement is used to create tha 'datacamp' database
cursor.execute("CREATE DATABASE datacamp")





#----------------------SHOW DATABASE_____
cursor = db.cursor()

# executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")

# 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

# printing the list of databases
print(databases)

# showing one by one database
for database in databases:
    print(database)


#-----------CREATING DB------------
cursor = db.cursor()

## creating a databse called 'datacamp'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'datacamp' database
cursor.execute("CREATE DATABASE datacamp")


#-----------CREATING TABLE---------
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "dbms",
    database = "datacamp"
)

cursor = db.cursor()

## creating a table called 'users' in the 'datacamp' database
cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")


#-------------DROP TABLE,CREATE PK--------
cursor = db.cursor()

## first we have to 'drop' the table which has already created to create it again with the 'PRIMARY KEY'
## 'DROP TABLE table_name' statement will drop the table from a database
cursor.execute("DROP TABLE users")

## creating the 'users' table again with the 'PRIMARY KEY'
cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")


#-------------Inserting Data-------------
## defining the Query
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
## storing values in a variable
values = ("Hafeez", "hafeez")

## executing the query with values
cursor.execute(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "record inserted")


#-------Inserting Multiple Rows-------
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
## storing values in a variable
values = [
    ("Peter", "peter"),
    ("Amy", "amy"),
    ("Michael", "michael"),
    ("Hennah", "hennah")
]

## executing the query with values
cursor.executemany(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "records inserted")


#-------------Select Data-----------
query = "SELECT * FROM users"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)
(1, 'Hafeez', 'hafeez')
(2, 'Peter', 'peter')
(3, 'Amy', 'amy')
(4, 'Michael', 'michael')
(5, 'Hennah', 'hennah')


#-----------Where________
query = "SELECT * FROM users WHERE id = 5"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)







