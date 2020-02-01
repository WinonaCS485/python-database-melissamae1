import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='lg6757bu',
                             password='password',
                             db='lg6757bu_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        #sql = "SELECT * from Students"
        
        # execute the SQL command
        #cursor.execute(sql)
        
        # get the results
        #for result in cursor:
            #print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()

        #search by user input
        name = input("Enter a first name to search: ")

        # execute the SQL command
        cursor.execute("SELECT * from Students WHERE firstName LIKE %s", (name,))
            
        # get the results
        for result in cursor:
            print (result)

finally:
    connection.close()




