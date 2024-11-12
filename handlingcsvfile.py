# IMPORT PATH TO CHECK THE EXISTING FILE 
from os import path
import csv
from userinput import keyboardInput

filename = "products.csv"

# OPEN AND CLOSE FILE
def create(filename):
    if not path.exists(filename): # it will check does the file exist or not?
        try:
            handler = open(filename, "xt") # if the doesn't exist, it will create a new file
            handler.close()
            createColumns(filename) # only for the first time when the file does'not exist
        except:
            print("Sorry unable to create the file")

# CREATE COLUMN TITLE (MODE W)
def createColumns(filename):
    try:
        with open(filename, "wt", newline='') as handler:
            csv_writter = csv.writer(handler, delimiter="|")
            csv_writter.writerow(["Product Name", "Quantity", "Price"]) # Pass list which has 3 values as an arguments
    except:
        print("Not able to create the column header")

# TAKE INPUT FROM USER AND APPEND THE DATA INSIDE THE FILE (INSERT PRODUCT)(MODE A)
def createProducts(filename):
    productname = keyboardInput("Product Name: ", str, "Product Name must be String")
    quantity = keyboardInput("Quantity: ", int, "Quantity must be Integer")
    price = keyboardInput("Price: ", float, "Price must be Float")
    try:
        with open(filename, "at", newline='') as handler:
            csv_writter = csv.writer(handler, delimiter="|")
            csv_writter.writerow([productname, quantity, price]) #Pass list of values and use writerow method
    except:
        print("Not able to append a product")

# READ DATA INSIDE THE FILE (MODE R)
def listProducts(filename):
    try:
        with open(filename, "rt", newline='') as handler:
            csv_reader = csv.reader(handler, delimiter="|") #this guys read everything for us. no need read in lines.
            print("=" * 67)
            for index, data in enumerate(csv_reader): #enumerate() give output tuple in list with 2 values (index, data)
                product, quantity, price = data #we don't need to split or strip because it already separated
                if (index == 0):
                    print(f"{product:40s}{quantity:>12s}{price:>15s}")
                    print("=" * 67)
                else:
                    print(f"{product:40s}{int(quantity):12d}{float(price):15.2f}")
            print("=" * 67)
    except Exception as e:
        print("Not able to read the file", e)

# EDIT PRODUCT LINES
def editProduct(filename):
    try:
        # open the file in read mode and get all the products
        with open(filename, "rt") as handler:
            reader = csv.reader(handler, delimiter="|") #you will get list of list after csv read
            csv_reader = list(reader) #you can assign it to another variable because python throw an error of I/O
        # find the index of the product which we want to edit
        producttoedit = keyboardInput("Enter the product to edit: ", str, "Product must be sring")
        productindex = None
        for index, item in enumerate(csv_reader):
            product, quantity, price = item
            if (product == producttoedit): 
                productindex = index
                break
        if (productindex != None): #If we want to edit but the item is not in the existing list. so we can do these for safe
            # Get the product details and update the list
            productname = keyboardInput(f"Product Name [{product}] : ", str, "Product Name must be String", product)
            quantity = keyboardInput(f"Quantity [{quantity}] : ", int, "Quantity must be Integer", quantity)
            price = keyboardInput(f"Price [{price}] : ", float, "Price must be Float", price)
            csv_reader[productindex] = [productname, quantity, price]
            with open(filename, "wt") as handler:
               csv_writter = csv.writer(handler, delimiter="|")
               csv_writter.writerows([productname, quantity, price]) #writerows read list of lists
        else:
            print("Product not found") #It will say the input product are not listed in existing list
    except Exception as e:
        print("An error occured while updating the product", e)

# DELETE PRODUCT
def deleteProduct(filename):
    try:
    # open the file in read mode and get all the products
        with open(filename, "rt") as handler:
            reader = csv.reader(handler, delimiter="|") #list of lists
            products = list(reader)
        # find the index of the product which we want to edit
        producttoedit = keyboardInput("Enter the product to delete: ", str, "Product must be string")
        productindex = None
        for index, item in enumerate(products):
            product, quantity, price = item
            if (product == producttoedit): 
                productindex = index
                break
        if (productindex != None):
            print(f"Product: {product}")
            print(f"Quantity: {quantity}")
            print(f"Price: {price}")
            confirm = keyboardInput("Are you sure (Y/N): ", str, "Confirm must be string")
            if (confirm == "Y"):
                del products[productindex]
                with open(filename, "wt", newline='') as handler:
                    csv_writter = csv.writer(handler, delimiter="|")  
                    csv_writter.writerows(products)             
        else:
            print("Product not found")
    except Exception as e:
        print("An error occured while updating the product", e)

def doMenu():
    choice = -1
    while (choice != 0):
        print("===================")
        print("|1. List Products |")
        print("|2. Create Product|")
        print("|3. Edit Product  |")
        print("|4. Delete Product|")
        print("|0. Exit          |")
        print("===================")
        choice = keyboardInput("Enter your choice: ", int, "Choice must be Integer")
        if (choice == 1):
            listProducts(filename)
        elif (choice == 2):
            createProducts(filename)
        elif (choice == 3):
            editProduct(filename)
        elif (choice == 4):
            deleteProduct(filename)
        elif (choice == 0):
            print("Thank you")
        else:
            print("Choice can be [0, 1, 2, 3] only")

create(filename)
doMenu()

# create(filename)
# createProducts(filename)
# listProducts(filename)