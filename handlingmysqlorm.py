# STORE DATA USING ORM

from userinput import keyboardInput
# pip3 install SQLAlchemy
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Products

def getDbConnection(host, username, password, database):
    url = f"mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}"
    engine = create_engine(url)
    return engine

def createProducts(engine):
    # sessionmaker is a function that takes engine 
    # and returns the class Session
    Session = sessionmaker(bind=engine)
    # le us create session object
    session = Session()

    productname = keyboardInput("Product Name: ", str, "Product Name must be String")
    quantity = keyboardInput("Quantity: ", int, "Quantity must be Integer")
    price = keyboardInput("Price: ", float, "Price must be Float")
    product = Products(name = productname, quantity = quantity, price = price)
    session.add(product)
    session.commit()

def listProducts(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.execute(select(Products)).scalars().all()
    try:
        # now the data is in the cursor
        print("=" * 85)
        print(f"{'Id':10s}{'Name':40s}{'Quantity':>15s}{'Price':>20s}")
        print("=" * 85)
        for product in rows:
            print(f"{int(product.id):<10d}{product.name:40s}{int(product.quantity):15d}{float(product.price):20.2f}")
        print("=" * 85)
    except Exception as e:
        print("Not able to read the file", e)

def editProduct(engine):
    productid = keyboardInput("Enter product id: ", int, "Product Id must be integer")
    Session = sessionmaker(bind=engine)
    session = Session()
    product = session.get(Products, productid)
    try:
        id, name, quantity, price = product.id, product.name, product.quantity, product.price
    except:
        print("Product for this Id does not exists")
    else:
        name = keyboardInput(f"Product Name [{name}] : ", str, "Name must be String", name)
        quantity = keyboardInput(f"Quantity [{quantity}]: ", int, "Quantity must be Integer", quantity)
        price = keyboardInput(f"Price [{price}] : ", float, "Price must be Float", price)
        product = Products(id = productid, name = name, quantity = quantity, price = price)
        session.merge(product)
        session.commit()

def deleteProduct(engine):
    productid = keyboardInput("Enter product id: ", int, "Product id must be integer")
    Session = sessionmaker(bind=engine)
    session = Session()
    product = session.get(Products, productid)
    try:
        id, name, quantity, price = product.id, product.name, product.quantity, product.price
    except:
        print("Product for this Id does not exists")
    else:        
        print(f"Product: {name}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")
        confirm = keyboardInput("Are you sure (Y/N): ", str, "Confirm must be string")
        if (confirm == "Y"):
            session.delete(product)
            session.commit()

def doMenu(engine):
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
            listProducts(engine)
        elif (choice == 2):
            createProducts(engine)
        elif (choice == 3):
            editProduct(engine)
        elif (choice == 4):
            deleteProduct(engine)
        elif (choice == 0):
            print("Thank you")
        else:
            print("Choice can be [0, 1, 2] only")

try:
    engine = getDbConnection("localhost", "root", "", "ecatalog")
except Exception as e:
    print(e)

doMenu(engine)
 
