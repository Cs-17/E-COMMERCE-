import mysql.connector as conec 
def printer(disp):
    j=0
    for i in ("item code", "name", "description", "quantity","price", "category"):
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
        query = "select items from customers where ph={}".format(pNo)
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
        query = "update inventory set qty ={} where item_code = {}".format(qty,inp)
        curs.execute(query)
        if (items==None):
            items=str(inp)
            inpQty=inpQty-1
        items = items + (","+ str(inp))*inpQty
        items=str(items)
        print(items)
        query = """update customers set items= "{}" 
        where ph= {}""".format(items,pNo)
        curs.execute(query)
        handle.commit()

def cart (handle, pNo):
    curs=handle.cursor()
    query= 
def main (handle,pNo):
    while(1):
        inp=int(input("\n press 1 to view products and\n 2 to see cart"))
        if (inp==1):
            store(handle,pNo)
        elif (inp==2):
            cart(handle,pNo)

        