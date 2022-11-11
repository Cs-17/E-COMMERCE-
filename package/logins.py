import initialising as base
def admin():#login for admin
    adminPass="TEST"#set login info for admins
    adminPh=1234
    #yet to be encrypted

    try:
        phNo=int(input("Enter phone number"))
        pasw=input("Enter password")
    except TypeError: #if phone number input includes non digit characters
        print("retry")
        return (admin())
    if (phNo==adminPh and pasw==adminPass):#if login successful
        print("Logged in")
        return (1)
    else:
        print("retry")
        return (admin())
    