import os
import datetime                 #this allows a date/time in our column
import pymysql

# get username from cloud9 workspace
# modify this if running on another environment

username = os.getenv('C9_USER')

# connect to the database
#So we're saying host is localhost, user is the username variable that we set above, the password is, of course, still blank unless you have changed it, and we're going to use the Chinook database.
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    #run a query
    #we open a connection to the database and then we use that connection to create the cursor.
    #The cursor is the object that we actually use to execute queries.
    #Executing a query with a cursor will cause the query to run in the server, but it won't return the data to your application.
    #To do that, you need to fetch the data.
    with connection.cursor() as cursor:   # advantage of using the DictCursor is that the rows now include the column names.
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
                        #creates a table called friends, a name with up to 20 char,age,dob
        #note that the above will still display a warning (not error) if the table already exists
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
    
    