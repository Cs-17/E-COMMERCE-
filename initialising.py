import mysql.connector as m 
host1="localhost"
us= "cs"
passw="123456"
c=m.connect(host=host1,user =us,password=passw)
cur=c.cursor()
cur.execute ("create database if not exists shop1")
c=m.connect(host=host1,user =us,password=passw,database="shop1")
cur=c.cursor()
q= """CREATE TABLE IF NOT EXISTS INVENTORY(ITEM_CODE INT NOT NULL PRIMARY KEY, 
PRODUCT VARCHAR(30), 
DESCR VARCHAR(50), 
QTY INT, 
PRICE DOUBLE(6,2), 
DISC INT, 
CAT VARCHAR(10))"""
cur.execute (q)
q= """CREATE TABLE IF NOT EXISTS CUSTOMERS(
NAME VARCHAR(10),
PH INT NOT NULL PRIMARY KEY,
PASSWORD VARCHAR(20),
ITEMS VARCHAR(100));"""
cur.execute (q)
c.commit()
