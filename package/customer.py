import mysql.connector as conec 
import random
def printer(disp):
    j=0
    for i in ["ITEM CODE", "NAME", "DESCRIPTION", "QUANTITY","PRICE", "CATEGORY"]:
        print (i.ljust(15), end="")
    print()
    for i in disp:             
        for j in i:
            print (str(j).ljust(15), end="") 
        print()
def store(handle,pNo):
    curs=handle.cursor()
    query= """
    select cat from inventory;
    """
    curs.execute(query)
    disp=curs.fetchall()
    catList=[]
    for i in disp:
        catList.append(i[0])
    print ("categories are:-")
    for i in catList:print(i)
    inp=input("Enter category you want to see, 0 to see all products")
    if (inp=="0"):
        query="""select * from inventory;"""
    else:
        cat=inp
        query = """select * from inventory where cat = "{}" ;""".format(cat)
    curs.execute(query)
    disp=curs.fetchall()
    printer(disp)
    inp=int(input("Enter item number for product to be added to cart"))
    query= """select qty from inventory where item_code = {};""".format(inp)
    curs.execute(query)
    inpQty=int(input("Enter quantity to be added"))
    qty=(curs.fetchmany(1))[0][0]
    if (qty<inpQty):
        print ("Out of stock")
    else:
        query = "select items from customers where ph={};".format(pNo)
        curs.execute(query)
        items=((curs.fetchmany(1))[0][0])
        print (items)
        """for i in range (1, inpQty+1):
            it=(curs.fetchmany(1))[0][0]
            if (it==None):
                items=str(inp)
            else:
                items=items+","+str(inp)
        SAME THING AS BELOW BUT WITH LOOP, DOESN'T WORK FOR SOME REASON
        """
        qty=qty-inpQty
        query = "update inventory set qty ={} where item_code = {};".format(qty,inp)
        curs.execute(query)
        if (items==None):
            items=str(inp)
            inpQty=inpQty-1
        items = items + (","+ str(inp))*inpQty
        items=str(items)
        print(items)
        query = """update customers set items= "{};" 
        where ph= {}""".format(items,pNo)
        curs.execute(query)
        handle.commit()

def cart (handle, pNo):
    curs=handle.cursor()
    query= "select items from customers where ph = {};".format(pNo)
    curs.execute(query)
    items=curs.fetchall()[0][0]
    if (items==None):
        print ("No items in cart")
        store(handle,pNo)
    else:
        items=items.split(",")
    #print (items)
    query=""
    out=[]

    for i in items:
        query= ( "select * from inventory where item_code = {};".format(i))
        curs.execute(query)
        x=((curs.fetchmany(1))[0])
        out.append(x)

    out2=set(out)

    out3=[]
    for i in out2: 
        out3.append(list(i))

    qty=0
    for i in range(0,len(out3)):
        qty=0
        for j in out:
            if (out3[i][0]==j[0]):
                qty=qty+1
            out3[i][3]=qty

    if (len(out3)<7):
        print (out3)
        for i in range (0,len(out3)):
            out3[i].append(((out3[i])[3]*(out3[i])[4]))
    else:
        for i in range (0,len(out3)):
            out3[i][6]=(((out3[i])[3]*(out3[i])[4]))
    printer (out3)

    total = 0
    for i in out3: 
        total= total+ i[6]

    print ("Sub total is ", total)
    d=random.randrange(0,9)
    print ("You get a discount of {} %".format(d))
    print ("discounted total is", (1-(d/100))*total)
    print ("Taxed(18%) grand total is ", 1.18*total)

    inp=input("enter c to checkout\n0 to go back to store\n1 to go remove an item")
    if (inp.lower()=="c"):
        print ("THANK YOU FOR SHOPPING")
        query= "update customers set items = NULL where ph={};".format(pNo)
        curs.execute(query)
        handle.commit()
        quit()
    elif (inp=="0"):
        store(handle,pNo)
    elif (inp=="1"):
        printer (out3)
        inp = int(input ("Enter item code to remove"))
        intQty = int(input("Enter quantity to remove"))
        out=[]
        for i in range(0,len(out3)):
            if (out3[i][0]==inp):
                if (out3[i][3]>=inpQty):
                    query="""select items from customers where ph ={}""".format(pNo)
                    curs.execute(query)
                    out=(curs.fetchall()[0][0]).split()
                    for i in out and inpQty>0:
                        if (i==str(inp)):
                            inpQty-=1
                            continue
                        else:
                            out.append(i)
        print (out)

def main (handle,pNo):
    while(1):
        inp=int(input("\n press 1 to view products and\n 2 to see cart"))
        if (inp==1):
            store(handle,pNo)
        elif (inp==2):
            cart(handle,pNo)

        