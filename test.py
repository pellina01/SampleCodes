import mysql.connector

from mysql.connector import Error



#try:

connection = mysql.connector.connect(host='localhost',

database='db_sales',user='admin',password='password',buffered=True)

if connection.is_connected():

    db_Info = connection.get_server_info()

    print("Connected to MySQL Server version ", db_Info)

    cursor = connection.cursor()

    cursor.execute("select database();")

    record = cursor.fetchone()

    print("You're connected to database: ", record)
    item_id = input("enter item id")
    #description = input("enter item name")
    sell_price = input("enter sell price")
    cost_price = input("enter cost price")
    sql_select_Query = "update item set cost_price = %s, sell_price = %s where item_id = %s"

    cursor = connection.cursor()

    cursor.execute(sql_select_Query, (cost_price,sell_price,item_id))
    connection.commit()

  #  records = cursor.fetchall()

  #  print("Total number of rows in Laptop is: ", cursor.rowcount)

 #   print(records)

# print("\nPrinting each laptop record")

    #print(records[0],records[1])

##    for row in records:
##
##        print("first name = ", row[0] )
##
##        print("last name = ", row[1])
##
##        print("address  = ", row[2])
##
##        print("town = ", row[3], "\n")
##        
##        print("town = ", row[4], "\n")

    cursor.close()

##item = 'vans'
##
##sell_price = 45.90
##
##cost_price = 90.00
##
##discontinued = 0
##
##category_id = 3
##
##val = (item,sell_price,cost_price,discontinued,category_id)
##
##mySql_insert_query = """INSERT INTO item(description, sell_price, cost_price,discontinued,category_id)
##
##VALUES (%s, %s, %s,%s,%s) """
##
###cursor = connection.cursor(dictionary=True)
##
##cursor = connection.cursor()
##
#cursor.execute(mySql_insert_query,val)
##
##connection.commit()
##
print(cursor.rowcount, "Record inserted successfully into item table")
##
##print(cursor.lastrowid)
##
##id = int(input('enter id'))
##
##sql_Delete_query = """Delete from item where item_id = %s"""
##
##cursor.execute(sql_Delete_query, (id,))
##
##connection.commit()
##
##print("Record Deleted successfully ")
##
##item_id = int(input('enter item id'))
##
##price = int(input('enter price'))
##
##sql_update_query = """Update item set sell_price = %s where item_id = %s"""
##
##inputData = (price,item_id)
##
##cursor.execute(sql_update_query, inputData)
##
##connection.commit()
##
##print("Record Updated successfully ")
##
### cursor.close()
##
##
##
###cursor = connection.cursor() where item_id = %s ,itemid
##
##itemid = int(input('enter item id'))
##
##sql_select_Query = """select * from item where item_id = %s or item_id = %s"""
##
##cursor.execute(sql_select_Query,(itemid,3))
##
##records = cursor.fetchall()
##
##print("Total number of rows in Laptop is: ", cursor.rowcount)
##
##print(records)
##
##print("\nPrinting each laptop record")
##
###print(records[2])
##
##for row in records:
##
##print("Id = ", row['item_id'] )
##
##print("Name = ", row['description'])
##
##print("Price  = ", row['sell_price'])
##
##print("Purchase date  = ", row['cost_price'], "\n")
##
##

##except Error as e:
##
##print("Error while connecting to MySQL", e)
##
##finally:
##
##if (connection.is_connected()):
##
##cursor.close()

connection.close()

print("MySQL connection is closed") 