#this script calls all subsidiaries
import initialising as base #initialisation for sql
import logins #methods to log customers and admin in
import admins 
import customer
handle=base.make()
consnt= input("Are you an admin?") #checks if admin or customer

if ("y" in consnt.lower()): #case:admin
    print("doing admin login")
    if (logins.admin()): #if login valid
        admins.main(handle) # admin functions
else:
    pNo=logins.customer(handle)
    if (pNo): # customer login success
        customer.main(handle,pNo)

