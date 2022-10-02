import initialising as base
import GUIhandler
import logins
#GUIhandler.makeWindow()
base.make()
#wndw.mainloop()
consnt= input("Are you a customer?")
if ("n" in consnt.lower()):
    print("doing admin login")
    x=logins.admin()
    print (x)
else:
    x=logins.custo()
