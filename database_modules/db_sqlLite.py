#sqlite3, DB API for SQLite database
#SQLite is a very lightweight database
import Constants
import sqlite3
# establishing  a database connection
con = sqlite3.connect(Constants.DATA_TEST_DB_1)
# preparing a cursor object
cursor = con.cursor()
# preparing sql statements to create table
sql1 = 'DROP TABLE IF EXISTS EMPLOYEE'
sql2 = '''CREATE TABLE EMPLOYEE (EMPID INT(6) NOT NULL,NAME CHAR(20) NOT NULL,AGE INT,SEX CHAR(1),INCOME FLOAT)'''
# executing sql statements
cursor.execute(sql1)
cursor.execute(sql2)
# closing the connection
con.close()
# preparing sql statements to insert data
con = sqlite3.connect(Constants.DATA_TEST_DB_1)
cursor = con.cursor()
sql3 = '''INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)'''
rec = [12,'Rahul Acharya',33,'M',1000000]
# executing sql statement using try ... except blocks
# inserting one record
try:
    cursor.execute(sql3, rec)
    con.commit()
except Exception as e:
    print("Error Message :", str(e))
    con.rollback()

recs = [(13,'Luhar Acharya',31,'M',2000000),
        (14,'Karthik Acharya',33,'M',3000000),
        (15,'Shulka Acharya',30,'F',7000000),]
#inserting multiple records  (updates can be made similarly)
try:
    cursor.executemany(sql3, recs)
    con.commit()
except Exception as e:
    print("Error Message :", str(e))
    con.rollback()
con.close()


### Fetching records from table
con = sqlite3.connect(Constants.DATA_TEST_DB_1)
# preparing a cursor object
cursor = con.cursor()
sql4 = 'select * from EMPLOYEE'
try:
    cursor.execute(sql4)
except:
    print('Unable to fetch data.')
####Fetching one record as a tuple
print("Fetching one record")
rec = cursor.fetchone()
print(rec)
#### Fetching multiple records as tuple of tuples
print("Fetching rest of the records")
recs = cursor.fetchall()
for i in recs:
    print(i)

con.close()

#######################################
## CONTEXT MANAGER
#######################################
## Allows a programmer to perform required activities, 
## automatically, while entering or exiting a Context.
###########################
## Opening a file, doing few file operations, and closing 
## the file is manged using Context Manager as shown below.
with open(Constants.DATA_TXT_FILE_1, 'r') as fp:
    content = fp.read()
print("file content is: "+content)
## keyword 'with' helps enable a context manager. 
## It automatically takes care of closing the file.
#######################################
## Another example - no need to close conn
class DbConnect(object):
    def __init__(self, dbname):
        self.dbname = dbname
    def __enter__(self):
        self.dbConnection = sqlite3.connect(self.dbname)
        return self.dbConnection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbConnection.close()

with DbConnect(Constants.DATA_TEST_DB_1) as db:
    cursor = db.cursor()
    cursor.execute('select * from EMPLOYEE')
    recs = cursor.fetchall()
print("Printing all records from Context manager")
print(recs)

######################################
