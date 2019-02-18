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
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection, regardless of whether the above was successful
    connection.close()
    
    