import mysql.connector as m 
from tkinter import *
from tkinter import messagebox
from tkinter import Label
from tkinter import ttk
import tkinter as t

def make():
    makeDB()
    makeTables()
    makeWindow()
    confirm()
def makeDB():
    host1="localhost"
    us= "cs"
    passw="123456"
    global c,cur
    c=m.connect(host=host1,user =us,password=passw)
    cur=c.cursor()
    cur.execute ("create database if not exists shop1")
    c=m.connect(host=host1,user =us,password=passw,database="shop1")
    cur=c.cursor()
def makeTables():
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
def makeWindow():
    print()
    global w
    w=t.Tk()
    w.title("Shop Manager")
    w.config(bg="#6883BC")
    
def confirm():
    c.commit()
    l=Label(w,text="Initialisation complete",font=("Cambria",40),bg="#6883BC",fg="#8A307F", ).pack(side="top",padx=10,pady=10)
    w.mainloop()

