import mysql.connector as conec 
import random
#prints a table of items
def printer(disp):
    j=0
    #header
    for i in ["ITEM CODE", "NAME", "DESCRIPTION", "QUANTITY","PRICE", "CATEGORY"]:
        print (i.ljust(20), end="")
#list of list printers
    print()
    for i in disp:             
        for j in i:
            print (str(j).ljust(20), end="") 
        print()

def store(handle,pNo):
    curs=handle.cursor()

    #extract list of categories
    query= """
    select cat from inventory;
    """
    curs.execute(query)
    disp=curs.fetchall()
    catList=[]
    #clean list
    for i in disp:
        catList.append(i[0])
    print ("categories are:-")
    
    #get unique categories from list
    catList=list(set(catList))

    #add category for all
    catList.append("all")
    for i in catList:print(i)
    inp=input("Enter category you want to see")

    #show all items
    if (inp.lower()=="all"):
        query="""select * from inventory;"""
    
    # show items category wise
    else:
        cat=inp
        query = """select * from inventory where cat = "{}" ;""".format(cat)
    curs.execute(query)
    disp=curs.fetchall()
    printer(disp)

    #get what to add into cart
    #get avaialble quantity
    inp=int(input("Enter item number for product to be added to cart"))
    query= """select qty from inventory where item_code = {};""".format(inp)
    curs.execute(query)
    qty=(curs.fetchmany(1))[0][0]

    #get req. qty
    inpQty=int(input("Enter quantity to be added"))
    if (qty<inpQty):#checks if in stock
        print ("Out of stock")
        store(handle,pNo)
    else:
        query = "select items from customers where ph={};".format(pNo)
        curs.execute(query)
        items=((curs.fetchmany(1))[0][0])#extract integer from list of tuples
        #print (items)
        """for i in range (1, inpQty+1):
            it=(curs.fetchmany(1))[0][0]
            if (it==None):
                items=str(inp)
            else:
                items=items+","+str(inp)
        SAME THING AS BELOW BUT WITH LOOP, DOESN'T WORK FOR SOME REASON
        """
        #soft update quantity available
        qty=qty-inpQty

        #hard set qty 
        query = "update inventory set qty ={} where item_code = {}".format(qty,inp)
        curs.execute(query)


        #adding to cart
        
        #if first run and cart is empty
        if (items==None):
            items=str(inp) 
            inpQty=inpQty-1
        items = items + (","+ str(inp))*inpQty   #add the items to string of items as many times as req
        items=str(items) #convert to string
        #print(items)

        #hard update customer cart items
        query = """update customers set items= "{}" 
        where ph= {}""".format(items,pNo)
        curs.execute(query)
        handle.commit()

#out3 is array of table of cart items
def remover(out3, handle, pNo):
    curs=handle.cursor()
    printer (out3)

    inp = int(input ("Enter item code to remove"))
    inpQty = int(input("Enter quantity to remove"))

    out=[]
    out2=""

    # for each item entry
    for i in range(0,len(out3)):

        #if item code is as entered
        if (out3[i][0]==inp):

            #if the removal requirement is <= that in cart
            if (out3[i][3]>=inpQty):

                query="""select items from customers where ph ={} ;""".format(pNo)
                curs.execute(query)
                out=(curs.fetchall()[0][0]).split()

                #itemList contains all non unique item numbers
                itemList=out[0].split(",")
                print(itemList)

                #for as many times removal is required, remove said item
                for i in range (0,inpQty):
                    itemList.remove(str(inp))

                #make an array from edited list
                for i in itemList:
                    out2+=(i + ",")
                #clean out last comma
                out2=out2[:len(out2)-1]

    #write to table new item list
    query= """
    update customers set items= "{}" where ph= {} ;
    """.format(out2, pNo)
    curs.execute(query)
    query= """update inventory set qty =qty+{} where item_code= {}""".format(inpQty, inp)
    curs.execute(query)
    handle.commit()
def cart (handle, pNo):
    curs=handle.cursor()

    #get current cart entires
    query= "select items from customers where ph = {} ;".format(pNo)
    curs.execute(query)
    items=curs.fetchall()[0][0]
    if (items==None):
        #if no items report and return to store
        print ("No items in cart")
        store(handle,pNo)
    else:
        #break items into list
        items=items.split(",")
    #print (items)

    query=""
    out=[]

    for i in items:
        #extract item codes form list and make  tuples of all said product details
        query= ( "select * from inventory where item_code = {} ;".format(i))
        curs.execute(query)
        x=((curs.fetchmany(1))[0])
        out.append(x) #add said tuple to list to make a list of all details of items in cart

    out2=set(out) #get dictionary of unique values in list

    out3=[]
    for i in out2: #convert ditionary to list
        out3.append(list(i))

    qty=0
    #check between original list and unique value list to get quanity of each item in cart
    for i in range(0,len(out3)):
        qty=0
        for j in out:
            if (out3[i][0]==j[0]):
                qty=qty+1
            out3[i][3]=qty #inject quantity of an item in cart into unique list  (previously had qty in inventory due to soft copy)


# add entry for total for whole qty of an item into unique cart list

    #first run, append entry lists and then do job for each entry
    if (len(out3)<7):
        print (out3)
        for i in range (0,len(out3)):
            out3[i].append(((out3[i])[3]*(out3[i])[4]))
    else:
        #do job i.e multiple qty and price
        for i in range (0,len(out3)):
            out3[i][6]=(((out3[i])[3]*(out3[i])[4]))
    printer (out3)

    #make grand total of base prices
    total = 0
    for i in out3: 
        total= total+ i[6]

    print ("Sub total is ", total)
    d=random.randrange(0,9) #get randomised discount 0-10
    print ("You get a discount of {} %".format(d))
    print ("discounted total is", (1-(d/100))*total)
    print ("Taxed(18%) grand total is ", 1.18*total)

    inp=input("enter c to checkout\n0 to go back to store\n1 to go remove an item")
    
    # options after showing cart
    if (inp.lower()=="c"): #checkout
        print ("THANK YOU FOR SHOPPING")
        query= "update customers set items = NULL where ph={} ".format(pNo)
        curs.execute(query) #clear items for that customer
        #add total to sales in future edit
        handle.commit()
        quit()
    elif (inp=="0"): #return to store
        store(handle,pNo)
    elif (inp=="1"):
        remover(out3,handle,pNo)
        
def main (handle,pNo):
    while(1):
        inp=int(input("\n press 1 to view products and\n 2 to see cart"))
        if (inp==1):
            store(handle,pNo)
        elif (inp==2):
            cart(handle,pNo)

        