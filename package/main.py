#this script calls all subsidiaries
import initialising as base #initialisation for sql
import GUIhandler # handler for ui/ux using tkinter
import logins #methods to log customers and admin in
import admins 
##GUIhandler.makeWindow()
base.make()
##wndw.mainloop()
consnt= input("Are you a customer?") #checks if admin or customer
if ("n" in consnt.lower()): #case:admin
    print("doing admin login")
    if (logins.admin()): #if login valid
        admins.main() # admin functions
else:
    x=logins.custo() # customer login
