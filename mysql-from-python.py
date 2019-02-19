import os
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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:   # advantage of using the DictCursor is that the rows now include the column names.
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:      
            print(row)
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
    
    