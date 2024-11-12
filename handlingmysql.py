# HOW TO CONNECT MYSQL DATABASE TO PYTHON APPLICATION USING MYSQL CONNECTOR (DB DRIVER) - 
# Here we use official third-party package repository which is pypi.org for Python Package Index.
# Search for third party libraries is pip3 install mysql-connector-python 9.0.0

# THIS IS MAIN THIRD PARTY LIBRARIES OF PYTHON. DON'T DEPEND AND EXPECT ALL THIS METHOD WILL OCCUR SAME ON FUTURE   
# NOT ALL METHOD ARE FIXED BASED ON THIRD PARTY LIBRARIES (APPLICATION SIDE). EVERYDAY WILL CHANGES
# IT'S DOESN'T REMAINED. WE HAVE TO EXPLORE AND STUDY OUR OWNSELF. LIBRARIES WILL ALWAYS CHANGES.
# THE CONCEPT IS ALL SAME IN DATABASE. PLEASE REMEMBER. BUT THE CODING METHOD IS DIFFERENT.

# 1)mysql.connector.connect() => Python Application to MySQL Connector Python
# 2)Connection request        => MySQL Database to MySQL Connector Python
# 3)connection.cursor()       => Python Application to MySQL Connector Python
# 4)connected                 => MySQL Database to MySQL Connector Python 
# 5)Cursor.execute()          => Python Application to MySQL Connector Python
# 6)result data               => MySQL Database to MySQL Connector Python

# Different RDBMS. Different database different code but the idea and concepts is SAME.

from userinput import keyboardInput
# pip install mysql-connector-python
import mysql.connector as mysql

def getDbConnection(host, username, password, database):
    connection = mysql.connect(
        host = host,
        user = username,
        password = password,
        database = database)
    return connection

# HOW TO INSERT PRODUCTS IN THE DATABASE
def createProducts(connection):
    productname = keyboardInput("Product Name: ", str, "Product Name must be String")
    quantity = keyboardInput("Quantity: ", int, "Quantity must be Integer")
    price = keyboardInput("Price: ", float, "Price must be Float")
    try:
        SQL = f"""INSERT INTO products (name, quantity, price) 
                VALUES ('{productname}', {quantity}, {price})"""
        cursor = connection.cursor()
        cursor.execute(SQL)
        # to make it permanently inserted call commit method
        connection.commit()
    except Exception as e:
        print("Not able to append a product", e)

def listProducts(connection):
    try:
        SQL = "SELECT id, name, quantity, price FROM products"
        # In python to executed SQL you must create cursor from the connection
        cursor = connection.cursor()
        cursor.execute(SQL)
        # now the data is in the cursor
        print("=" * 85)
        print(f"{'Id':10s}{'Name':40s}{'Quantity':>15s}{'Price':>20s}")
        print("=" * 85)
        for id, name, quantity, price in cursor:
            print(f"{int(id):<10d}{name:40s}{int(quantity):15d}{float(price):20.2f}")
        print("=" * 85)
    except Exception as e:
        print("Not able to read the file", e)

# HOW TO PULL OUT THE DATA. NOW DATA IN THE CURSOR
def editProduct(connection):
    productid = keyboardInput("Enter product id: ", int, "Product Id must be integer")
    SQL = f"SELECT id, name, quantity, price FROM products WHERE id = {productid}"
    cursor = connection.cursor()
    cursor.execute(SQL)
    try:
        (id, name, quantity, price) = cursor.fetchone()
    except:
        print("Product for this Id does not exists")
    else:
        name = keyboardInput(f"Product Name [{name}] : ", str, "Name must be String", name)
        quantity = keyboardInput(f"Quantity [{quantity}]: ", int, "Quantity must be Integer", quantity)
        price = keyboardInput(f"Price [{price}] : ", float, "Price must be Float", price)
        SQL = f"""UPDATE products SET name = '{name}', quantity = {quantity}, price = {price}
                    WHERE id = {id}"""
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()

def deleteProduct(connection):
    productid = keyboardInput("Enter product id: ", int, "Product id must be integer")
    SQL = f"SELECT id, name, quantity, price FROM products WHERE id = {productid}"
    cursor = connection.cursor()
    cursor.execute(SQL)
    try:
        (id, name, quantity, price) = cursor.fetchone()
    except:
        print("Product for this Id does not exists")
    else:
        print(f"Product: {name}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")
        confirm = keyboardInput("Are you sure (Y/N): ", str, "Confirm must be string")
        if (confirm == "Y"):
            SQL = f"DELETE FROM products where id = {id}"
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

def doMenu(connection):
    choice = -1
    while (choice != 0):
        print("======================")
        print("| 1. List Products   |")
        print("| 2. Create Product  |")
        print("| 3. Edit Product    |")
        print("| 4. Delete Product  |")
        print("| 0. Exit            |")
        print("======================")
        choice = keyboardInput("Enter your choice: ", int, "Choice must be Integer")
        if (choice == 1):
            listProducts(connection)
        elif (choice == 2):
            createProducts(connection)
        elif (choice == 3):
            editProduct(connection)
        elif (choice == 4):
            deleteProduct(connection)
        elif (choice == 0):
            print("Thank you")
        else:
            print("Choice can be [0, 1, 2] only")

connection = getDbConnection("localhost", "root", "xs2p0rt4l", "ecatalog")
doMenu(connection)
