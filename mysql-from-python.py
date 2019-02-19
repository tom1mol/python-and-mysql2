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
   
    with connection.cursor() as cursor:   # advantage of using the DictCursor is that the rows now include the column names.
        row = ("Bob", 21, "1990-02-06 23:04:56")         #values stored in a tuple called row
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)  #cursor unpacks tuple.   %s represents each item in tuple
        connection.commit()                
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
    
    