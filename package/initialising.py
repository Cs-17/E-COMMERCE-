import mysql.connector as conec 

import GUIhandler

def make():
    makeDB()
    makeTables()
    #makeWindow()
    confirm()
def makeDB():
    host1="localhost"
    us= "cs"
    passw="123456"
    global handle,cur
    handle=conec.connect(host=host1,user =us,password=passw)
    cur=handle.cursor()
    cur.execute ("create database if not exists shop1")
    handle=conec.connect(host=host1,user =us,password=passw,database="shop1")
    cur=handle.cursor()
def makeTables():
    query= """CREATE TABLE IF NOT EXISTS INVENTORY(ITEM_CODE INT NOT NULL PRIMARY KEY, 
    PRODUCT VARCHAR(30), 
    DESCR VARCHAR(50), 
    QTY INT, 
    PRICE DOUBLE(6,2), 
    DISC INT, 
    CAT VARCHAR(10))"""
    cur.execute (query)
    query= """CREATE TABLE IF NOT EXISTS CUSTOMERS(
    NAME VARCHAR(10),
    PH INT NOT NULL PRIMARY KEY,
    PASSWORD VARCHAR(20),
    ITEMS VARCHAR(100));"""
    cur.execute (query)
'''def makeWindow():
    print()
    global wndw
    wndw=t.Tk()
    wndw.title("Shop Manager")
    global universalBg,universalFont
    universalBg="#8399c9"
    universalFont="Century Gothic"
    wndw.config(bg=universalBg)'''
    
def confirm():
    handle.commit()
    #GUIhandler.done()
    print("Done")

