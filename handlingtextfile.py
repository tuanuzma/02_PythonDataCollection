# 1. Open or Create a file
# 2. Write into the file
# 3. Read from the file
# 4. Close the file (not delete)

# Why we have to close the file ?

# If you open the file and did not close the file
# operating system will not let any other process
# to open that file. So you must close after you
# use that file

# To handle the files there are various modes
# You have to open the file with specific mode
# 1. To create a file you have to use the mode (x) 
# When you use the mode (x) python create the specified file. 
# If the file already exists it will throw us an error
# 2. To write into a file we have use the mode (w)
# When we use the mode (w) if the file does not exists
# python will create it. But if the file already exists
# python will erase the content inside the file and opens it
# 3. To append data inside the file we have to use the mode (a)
# When we use the mode (a) if the file does not exists
# python will create it. If the file already exists 
# it will not erase the content inside the file.
# 4. To read data inside the file we have to use the mode (r)


# we do have some extra modes
# 1. t stands for text file
# 2. b stands for binary file

# IMPORT PATH TO CHECK THE EXISTING FILE 
from os import path
from userinput import keyboardInput

filename = "products.dat"

# OPEN AND CLOSE FILE
def create(filename):
    # In python to open a file we have a built in function called open
    # open built in function takes 2 parameters filename, mode
    # if the file already exist it throw us the error
    # opening a file is an I/O operation
    if not path.exists(filename):
        try:
            # open is a built in function that returns the file object
            # which is assigned to a variable handler
            handler = open(filename, "xt")
            # However close is not a buit in function
            # close is a method
            handler.close()
            createColumns(filename) # only for the first time when the file does'not exist
        except:
            print("Sorry unable to create the file")

# CREATE COLUMN TITLE (MODE W)
def createColumns(filename):
    # Let us create column titles inside the file
    try:
        # there is always a high chance of the file not being closed
        # for some reason eventhough you have handler.close
        # In the latest python they introduce a block called "with"
        # with is a keyword
        # when you handle resource like file it is recomended to use
        # with block so that you no need to close the resource
        # it will be closed automatically when we come out 
        # of the with block
        with open(filename, "wt") as handler:
            # write i a method inside the file object
            handler.write("Product Name|Quantity|Price")
    except:
        print("Not able to create the column header")

# TAKE INPUT FROM USER AND APPEND THE DATA INSIDE THE FILE (INSERT PRODUCT)(MODE A)
def createProducts(filename):
    # Let us take input from the user and append the data inside the file
    productname = keyboardInput("Product Name: ", str, "Product Name must be String")
    quantity = keyboardInput("Quantity: ", int, "Quantity must be Integer")
    price = keyboardInput("Price: ", float, "Price must be Float")
    try:
        with open(filename, "at") as handler:
            handler.write(f"\n{productname}|{quantity}|{price}")
    except:
        print("Not able to append a product")

# READ DATA INSIDE THE FILE (MODE R)
def listProducts(filename):
    try:
        with open(filename, "rt") as handler:
            content = handler.readlines() # all the lines will be assigned to content variables #content give list of lines as output
            print("=" * 67)
            for index, data in enumerate(content): #enumerate() give output tuple in list with 2 values (index, data)
                product, quantity, price = data.strip().split("|")
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
            products = handler.readlines()
        # find the index of the product which we want to edit
        producttoedit = keyboardInput("Enter the product to edit: ", str, "Product must be sring")
        productindex = None
        for index, item in enumerate(products):
            product, quantity, price = item.strip().split("|")
            if (product == producttoedit): 
                productindex = index
                break
        if (productindex != None): #If we want to edit but the item is not in the existing list. so we can do these for safe
            # Get the product details and update the list
            productname = keyboardInput(f"Product Name [{product}] : ", str, "Product Name must be String", product)
            quantity = keyboardInput(f"Quantity [{quantity}] : ", int, "Quantity must be Integer", quantity)
            price = keyboardInput(f"Price [{price}] : ", float, "Price must be Float", price)
            products[productindex] = f"{productname}|{quantity}|{price}\n"
            # the last item (line) cannot have new line character
            products[-1] = products[-1].strip()
            with open(filename, "wt") as handler:
                handler.writelines(products)
        else:
            print("Product not found") #It will say the input product are not listed in existing list
    except Exception as e:
        print("An error occured while updating the product", e)

# DELETE PRODUCT
def deleteProduct(filename):
    try:
    # open the file in read mode and get all the products
        with open(filename, "rt") as handler:
            products = handler.readlines()
        # find the index of the product which we want to edit
        producttoedit = keyboardInput("Enter the product to edit: ", str, "Product must be sring")
        productindex = None
        for index, item in enumerate(products):
            product, quantity, price = item.strip().split("|")
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
                # the last item (line) cannot have new line character
                products[-1] = products[-1].strip()
                with open(filename, "wt") as handler:
                    handler.writelines(products)               
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
