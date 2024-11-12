# INSTALL pip3 install pymongo 4.8.0 in VSCode terminal
# MacOS using homebrew as third party package manager and install mongod and mongodb compass in terminal
from userinput import keyboardInput
from pymongo import MongoClient
from bson.objectid import ObjectId  # Convert string object id  to mongodb object

def getDbConnection(database):
    connection = MongoClient("mongodb://localhost:27017")
    db = connection[database]
    return db

# HOW TO INSERT PRODUCTS IN THE DATABASE
def createProducts(db):
    collection = db['products']
    productname = keyboardInput("Product Name: ", str, "Product Name must be String")
    quantity = keyboardInput("Quantity: ", int, "Quantity must be Integer")
    price = keyboardInput("Price: ", float, "Price must be Float")
    document = {
        "name": productname,
        "quantity": quantity,
        "price": price
    }
    collection.insert_one(document) #method, not use any sql here

# HOW TO PULL OUT THE TABLE
# Print id to edit or delete products from mongodb database
# Convert string object id  to mongodb object 
def listProducts(db):
    try:
        collection = db["products"]
        # now the data is in the collection
        print("=" * 105)
        print(f"{'Id':30s}{'Name':40s}{'Quantity':>15s}{'Price':>20s}")
        print("=" * 105)
        for document in collection.find():
            print(f"{str(document["_id"]):30s}{document["name"]:40s}{document["quantity"]:15d}{document["price"]:20.2f}")
        print("=" * 105)
    except Exception as e:
        print("Not able to read the file", e)

# HOW TO PULL OUT THE DATA. NOW DATA IN THE CURSOR
def editProduct(db):
    productid = keyboardInput("Enter product id: ", str, "Product Id must be string")
    collection = db['products']
    query = { "_id": ObjectId(productid) } # field in dictionary
    product = collection.find_one(query)
    try:
        id = product['_id']
        name = product['name']
        quantity = product['quantity']
        price = product['price']
    except:
        print("Product for this Id does not exists")
    else:
        name = keyboardInput(f"Product Name [{name}] : ", str, "Name must be String", name)
        quantity = keyboardInput(f"Quantity [{quantity}]: ", int, "Quantity must be Integer", quantity)
        price = keyboardInput(f"Price [{price}] : ", float, "Price must be Float", price)
        document = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        collection.update_one(query, {'$set': document}) # when you add query (new variable) and update in sets{}

# HOW TO DELETE PRODUCT
def deleteProduct(connection):
    productid = keyboardInput("Enter product id: ", str, "Product id must be string")
    collection = db['products']
    query = { "_id": ObjectId(productid) } # field in dictionary
    product = collection.find_one(query)
    try:
        id = product['_id']
        name = product['name']
        quantity = product['quantity']
        price = product['price']
    except:
        print("Product for this Id does not exists")
    else:
        print(f"Product: {name}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")
        confirm = keyboardInput("Are you sure (Y/N): ", str, "Confirm must be string")
        if (confirm == "Y"):
            collection.delete_one(query)


def doMenu(db):
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
            listProducts(db)
        elif (choice == 2):
            createProducts(db)
        elif (choice == 3):
            editProduct(db)
        elif (choice == 4):
            deleteProduct(db)
        elif (choice == 0):
            print("Thank you")
        else:
            print("Choice can be [0, 1, 2] only")

db = getDbConnection("ecatalog")
doMenu(db)
