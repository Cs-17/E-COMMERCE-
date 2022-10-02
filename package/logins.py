import initialising as base
def admin():
    adminPass="UngaBunga"
    adminPh=696969
    try:
        phNo=int(input("Enter phone number"))
        pasw=input(input("Enter password"))
    except TypeError:
        print("retry")
        return (admin())
    if (phNo==adminPh and pasw==adminPass):
        print("Logged in")
        return (1)
    else0:
        return (admin())
    
