#makes the db, tables and respective cursors.
import mysql.connector as conec 

def makeDB():
    host1="localhost"
    us= "cs"
    passw="123456"
    handle=conec.connect(host=host1,user =us,password=passw)
    curs =handle.cursor() #get cursor of sql without db
    curs.execute ("create database if not exists shop1")
    handle=conec.connect(host=host1,user =us,password=passw,database="shop1")
    curs=handle.cursor()#get cursor of db
    print ("database created.")
    handle.commit()
    return (handle)

def makeTables(handle):
    curs=handle.cursor()

    query= """CREATE TABLE IF NOT EXISTS 
    INVENTORY
    (ITEM_CODE INT NOT NULL PRIMARY KEY, 
    PRODUCT VARCHAR(30), 
    DESCR VARCHAR(50), 
    QTY INT, 
    PRICE DOUBLE(6,2),
    CAT VARCHAR(10))"""
    #DISC INT )"""
    
    #table inventory with item code, product name, description, quantity, price, discount, category
    
    curs.execute(query)
    #execute in sql
    
    print ("inventory table created")

    query= """CREATE TABLE IF NOT EXISTS 
    CUSTOMERS(
    NAME VARCHAR(10),
    PH INT NOT NULL PRIMARY KEY,
    PASSWORD VARCHAR(20),
    ITEMS VARCHAR(250));"""

    #Create table customers with name, phone number (used as identifier), pass and tuple of items in cart
    curs.execute(query)

    print ("customer table created")
    handle.commit()
    return (handle)

def defaultEntries(handle):
    curs=handle.cursor()
    query = """
        select * from customers;
    """
    curs.execute(query)
    out=curs.fetchall()
    if (out==[]):
        query = """insert into customers
        values
        ("rupam", 580792, "apples", "141,451,451,451,231"),
        ("ayush", 6746674, "bananas", "45,234,451,451,11"),
        ("anisha", 46969, "onion", "123,345,11,11,231"),
        ("chintu", 45643, "tree", "141,231,453,141,451"),
        ("anna", 88853, "grass", "312,664,664,664,231");
        """
        curs.execute(query)
        query = """insert into invewntory
        values
        ("rupam", 580792, "apples", "141,451,451,451,231"),
        ("ayush", 6746674, "bananas", "45,234,451,451,11"),
        ("anisha", 46969, "onion", "123,345,11,11,231"),
        ("chintu", 45643, "tree", "141,231,453,141,451"),
        ("anna", 88853, "grass", "312,664,664,664,231");
        """
        curs.execute(query)
        handle.commit()
        handle.commit()

def make():
 #caller for rest
    handle=makeDB()# makes the db if non existent

    handle=makeTables(handle) #makes tables if non existent
    defaultEntries(handle)
    print("done")
    return (handle)
