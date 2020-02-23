import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "admin",
    passwd = "123qwe",
    database="tkinter1"
)

cursor = db.cursor()
# execute 
cursor.execute("SHOW DATABASES")

# the list of databases is stored in 'databases'
databases = cursor.fetchall()

# who all databases in a single line: 
print(databases)

## show all databases line per line 
for database in databases:
    print(database)