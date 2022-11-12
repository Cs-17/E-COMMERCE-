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
    #make new account
    print("Account registration complete\n")



def customer(handle): #customer login
    curs=handle.cursor()
    try:
        pNo=int(input("Enter phone number"))#ask credentials
        pswd=input("Enter password")
    except:
        print("Wrong input")
        quit()
    query=""" 
    select * from customers where ph= {}
    """.format (pNo) 
    #get record of customers with given phne number
    curs.execute(query)
    disp=curs.fetchall()

    if (disp==[]):#if no record found
        newAcc(handle,pNo,pswd) #make new account
    elif (disp[0][2]!=pswd):
        print("wrong passsword")
        return (0)
        quit()
    else:
        return (pNo)
