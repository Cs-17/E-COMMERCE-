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

def newAcc(handle, pNo, pswd):
    curs=handle.cursor()
    name=input("Enter name, for new account registeration")
    query= """
    insert into customers VALUES ({},{},{},NULL);
    """.format(name,pNo,pswd)
    curs.execute(query)
    handle.commit()
    print("Account registration complete\n")
def customer(handle):
    curs=handle.cursor()
    pNo=int(input("Enter phone number"))
    pswd=input("Enter password")
    query="""
    select * from customers where ph= {}
    """.format (pNo)
    curs.execute(query)
    disp=curs.fetchall()
    print(disp)
    if (disp==[]):
        newAcc(handle,pNo,pswd)
    return (pNo)
