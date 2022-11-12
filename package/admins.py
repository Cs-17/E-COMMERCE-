import mysql.connector as conec 

def adder (handle):
    curs=handle.cursor()
    code=int(input("Enter item code"))
    product=input ("Enter product name")
    des=input ("Enter product description")
    qty= int(input("Enter available quantity"))
    price = float(input("Enter pricing") )
    cat= input("Enter category")
    query = """
    insert into inventory values({},{},{},{},{},{});
    """.format(code,product,des,qty,price,cat)
    curs.execute(query)
    handle.commit()

def disp(handle):
    #print the inventory table
    curs=handle.cursor()
    query="""
    select * from inventory;
    """
    print ("Current state of inventory table \n \n")
    curs.execute (query)
    x=curs.fetchall()
    for i in x: 
        print (i)

def deleter(handle,code):
    curs=handle.cursor()
    query=""" 
    DELETE from inventory 
    WHERE ITEM_CODE= {} ;
    """.format(code)
    curs.execute(query)
    handle.commit()

def mod(handle,code):
    curs=handle.cursor()
    text="""
    enter\n
    1 to edit name\n
    2 to edit price\n
    3 to edit description\n
    4 to edit quantity
    5. to edit category
    """
    inp=int(input(text))

    if (inp==1):
        inp=input("Enter new name for pre-entered code")
        query="""
        update inventory
        set product= {}
        where ITEM_CODE= {}
        """.format(inp,code)
        curs.execute(query)
        handle.commit()

    elif (inp==2):
        inp=float(input("Enter new price for pre-entered code"))
        query="""
        update inventory
        set price= {}
        where ITEM_CODE= {}
        """.format(inp,code)
        curs.execute(query)
        handle.commit()

    elif (inp==3):
        inp=input("Enter new description for pre-entered code")
        query="""
        update inventory
        set descr= {}
        where ITEM_CODE= {}
        """.format(inp,code)
        curs.execute(query)
        handle.commit()
        
    elif (inp==4):
        inp=int(input("Enter new quantity for pre-entered code"))
        query="""
        update inventory
        set qty= {}
        where ITEM_CODE= {}
        """.format(inp,code)
        curs.execute(query)
        handle.commit()
    elif (inp==5):
        inp=input("Enter new category for pre-entered code")
        query="""
        update inventory
        set cat= {}
        where ITEM_CODE= {}
        """.format(inp,code)
        curs.execute(query)
        handle.commit()
def main (handle):
    print ("reached admins()")
    while(1):
        disp(handle)
        #editor
        inp=input ("Enter item code to modify\nEnter 0 to add new item,\nenter x to exit")
        if (inp=="0"):
            adder(handle)
        elif (inp.upper()=="X"):
            break
        else:
            if (input ("enter 0 to delete\n1 to modify")=="0"):
                deleter(handle, int(inp))
            else:
                mod(handle,inp)
