#makes the db, tables and respective cursors.
import mysql.connector as conec 
global curs, handle
import GUIhandler
def makeDB():
    host1="localhost"
    us= "cs"
    passw="123456"
    handle=conec.connect(host=host1,user =us,password=passw)
    curs=handle.cursor() #get cursor of sql without db
    curs.execute ("create database if not exists shop1")
    handle=conec.connect(host=host1,user =us,password=passw,database="shop1")
    curs=handle.cursor()#get cursor of db
    print ("database created.")
def makeTables():
    query= """CREATE TABLE IF NOT EXISTS 
    INVENTORY
    (ITEM_CODE INT NOT NULL PRIMARY KEY, 
    PRODUCT VARCHAR(30), 
    DESCR VARCHAR(50), 
    QTY INT, 
    PRICE DOUBLE(6,2), 
    DISC INT, 
    CAT VARCHAR(10))"""
    #table inventory with item code, product name, description, quantity, price, discount, category
    curs.execute(query)#execute in sql
    print ("inventory table created")
    query= """CREATE TABLE IF NOT EXISTS 
    CUSTOMERS(
    NAME VARCHAR(10),
    PH INT NOT NULL PRIMARY KEY,
    PASSWORD VARCHAR(20),
    ITEMS VARCHAR(100));"""
    #Create table customers with name, phone number (used as identifier), pass and tuple of items in cart
    curs.execute(query)
    print ("customer table created")
def confirm():
    #GUIhandler.done()
    print("Done")
def make(): #caller for rest
    makeDB()# makes the db if non existent
    makeTables() #makes tables if non existent
    #makeWindow()
    handle.commit()
    confirm() #confirms if tables are made
make()
