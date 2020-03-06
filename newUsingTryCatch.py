import mysql.connector

from mysql.connector import Error



try:

    connection = mysql.connector.connect(host='localhost',

    database='db_sales',user='admin',password='password',buffered=True)

    if connection.is_connected():

        db_Info = connection.get_server_info()

        print("Connected to MySQL Server version ", db_Info)

        cursor = connection.cursor()

        cursor.execute("select database();")

        record = cursor.fetchone()

        print("You're connected to database: ", record)




##    cursor = connection.cursor(dictionary=True)
    cursor = connection.cursor()
    sql_select_Query = "select * from item"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)
    print(records)
    print("\nPrinting each laptop record")

    for row in records:
        print(row)
        print("Id = ", row['item_id'] )
        
        print("Name = ", row['description'])
        
        print("Price  = ", row['sell_price'])
        
        print("Purchase date  = ", row['cost_price'], "\n")



except Error as e:

    print("Error while connecting to MySQL", e)
##
finally:
##
    if (connection.is_connected()):
    ##
        cursor.close()

        connection.close()

    print("MySQL connection is closed") 
