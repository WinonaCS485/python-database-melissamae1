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

        #search by user input
        name = input("Enter a first name to search: ")
        sql = "SELECT * from Students WHERE firstName LIKE %s"

        # execute the SQL command
        cursor.execute(sql, (name,))
                
        # get the results
        for result in cursor:
            print (result)
                
            
finally:
    connection.close()  




