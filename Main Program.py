'''
                                        ****************************
                                            PROJECT :  CLOUD CAFE !
                                        ****************************

'''
import sys
import os
from os import system
import mysql.connector as cntr
import random
import csv
from tempfile import mktemp
from collections import Counter

con = cntr.connect(user= "root" , password = "Pisces", database = "ProjectXII")
cursor= con.cursor()
is_leapyear = lambda year : year % 4 == 0
def tdays_month(month , year):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month == 2 and is_leapyear(year):
        return 29
    elif month == 2:
        return 28
    else:
        return 30
    		           
def register():
    try:
        # db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=con.cursor()
        usrnm=input("Enter username: ")
        cur.execute("select count(*) from Staff where username = '{}'".format(usrnm))
        data = cur.fetchall()
        print("No of records with name = '",usrnm, "' is =", data[0][0])
        if data[0][0] >= 1:
            print("Already Registered")
        else:
            pwd=input("Enter password: ")
            pwd2=input("Enter password again to confirm: ")
            if pwd==pwd2:
                cur.execute("insert into Staff values ('{}' , '{}')".format(usrnm,pwd))
                con.commit()
                print("New User Added Sucessfully !!")
            else:
                print("Passwords don't match.")
    except Exception as e:
        print ("Unable to add user",e)
 
# Login as Staff
# Access to valid registeration only

def login():
    try:
        # db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=con.cursor()
        user = input("Enter the username : ")
        pwd = input("Enter the password : ")
        cur.execute("select count(*) from Staff where username = '{}' and password = '{}'".format(user ,pwd))
        rowcount= cur.fetchall()
        verify= rowcount[0][0]
        return (bool(verify))
    except:
        print ("Unable To Login")
# De-Register Ex-Staff info
# Delete

def exStaff():
    try:
        # db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=con.cursor()
        user = input("Enter the username to be removed: ")
        cur.execute("delete from Staff where username = '{}'".format(user))
        con.commit()
        print("Ex-Staff User Removed Sucessfully !!")
    except:
        print("Unable To Remove Ex-Staff")

# View stock available in the pantry

def view_prd():
    try:
        # db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=con.cursor()
        cur.execute("select Prd_id,Prd_Name,Available_Stock, Cost_per_piece from Products")
        data = cur.fetchall()
        con.commit()
        print("Product Id \t\tProduct Name\t\t Inventory\t\tCost")
        for row in data :
            print(row[0],'\t\t\t',row[1].ljust(24,' '),row[2] ,'\t\t\t' , row[3])
    except:
        print ("Unable to show the inventory details")
            
# Add Products
# Insert
        
def add_prd():
    try:
        #  db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=con.cursor()
        while True:
            prd_id=int(input("Enter prd id: "))
            prd_nm=input("Enter name: ")
            cost=float(input("Enter cost [%.xx]: "))
            stock=int(input("Enter stock: "))
            purchased=int(input("Enter qty purchased: "))
            prg = ("insert into Products values ({} , '{}' , {} , {} , {} )".format(prd_id , prd_nm , cost, stock , purchased))
            cur.execute(prg)
            con.commit()
            flag= input ("Continue? Y/N: ")
            flag=flag.upper()
            if flag=="N":
                view_prd()
                break
    except:
        print ("Unable to add the inventory details")
        
# Modify product table entries
# Update
def update_prd():
    try:
        # db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=con.cursor()
        while True:
            Prd_id = int(input("Enter the Product Id : "))
            cur.execute("select Prd_Id, Prd_Name , Available_Stock , Cost_per_piece from Products where Prd_Id = {}".format(Prd_id))
            data=cur.fetchall()
            if data ==[]:
                print("Sorry ",Prd_Name ," with product ID ",Prd_id," Not Available")
            else:
                print("Product ID: ", data[0][0])
                print("Product : " , data[0][1])
                print("Available Stock : " , data[0][2])
                print("Current Price : ", data[0][3])
                print("1. ADD to Inventory")
                print("2. Price Update")
                cq = int(input("Enter your choice : "))
                if cq == 1:
                    stock = float(input("Enter the new stock purchased : "))
                    qstock = 'update Products set Available_Stock = Available_Stock + %s WHERE Prd_Id = %s'
                    daqs = (stock, Prd_id)
                    cur.execute(qstock, daqs)
                    con.commit()
                elif cq == 2:
                    updatePrice = int(input("Enter the new selling price : "))
                    qcost = 'update Products set Cost_per_piece = %s WHERE Prd_Id = %s'
                    daqc = (updatePrice, Prd_id)
                    cur.execute(qcost, daqc)
                    con.commit()
                flag= input ("Continue with update? Y/N: ")
                flag=flag.upper()
                if flag=="N":
                    view_prd()
                    break
    except Exception as e:
        print ("Unable to update the inventory details",e)

# Generate and View Bill
# Insert and update
# File handling
# Tabular output

def takeout():
    try:
        # db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=con.cursor()
        print('========Take Order==========')
        r_no = random.randint(100,1000)
        print("Invoice No : ", r_no)
        pdate = input("Enter date (YYYY-MM-DD): ")
        cust_id = input("Enter Customer ID:")
        Cust_Name = input("Enter Customer Name : ")
        cur.execute("select cust_id, Cust_Name, Phone, Address from Customers where cust_id ={}".format(cust_id))
        data = cur.fetchall()
        print(data)
        if cur.rowcount == 1:
            print("Welcome *"+data[0][1]+"* Once Again!")
            Phone_No = data[0][2]
            Address = data[0][3]
            flag = 'y'
        else:
            Address = input("Enter Address : ")
            Phone_No = int(input("Enter Mobile No. : "))
        no_items = int(input("Enter number of items requested : "))
        bill_amt = 0.00
        while (no_items > 0):
                #pdate = _dt.date.today()
                print (" Item List :: ")
                cur.execute("select Prd_id,Prd_Name, Cost_per_piece from Products")
                data = cur.fetchall()
                con.commit()
                print("Product Id \t\tProduct Name \t\tCost")
                for row in data :
                    print(row[0],'\t\t\t',row[1].ljust(24,' '),row[2])
                
                #cur.execute("select Prd_Name, Prd_Id from Products")
                #data = cur.fetchall()
                #print(data)
                    
                #INPUT 
                prd_no = int(input("Enter Product Id : "))
                #prd_name = input("Enter the Item name : ")
                prd_qty = eval(input("Enter required quantity : "))
                cur.execute("select Prd_Name , Prd_Id , Cost_per_piece from Products where Available_Stock = 0 and Prd_Id = {}".format(prd_no))
                data = cur.fetchall()
                #print(data)
                if cur.rowcount == 1:
                    print("Sorry "+data[0][0]+" Not Available")
                    print()
                else:
                    cur.execute("select Prd_Name , Prd_Id , Cost_per_piece from Products where Prd_Id ={}".format(prd_no))
                    data = cur.fetchall()
                    #print(data)
                    prd_name = data[0][0]
                    subT=float(prd_qty*data[0][2])
                    print("Pay INR", subT)
                    bill_amt = bill_amt + 1.20 * subT
                    print ("Total bill : ", bill_amt)
                    #cur.execute("insert into Invoice (Receipt_no, Prd_id, Prd_Name,
                    # Qty_ordered,Sub_Total_Cost, Total_Bill_Amount,Cust_id, Purchased_on) values({} ,{},'{}', {}, {}, {}, {},
                    # '{}')".format(r_no, prd_no , prd_name, prd_qty ,subT , bill_amt , cust_id , pdate))
                    cur.execute("insert into Invoice (Receipt_no, Prd_id, Prd_Name, Qty_ordered,Sub_Total_Cost, Total_Bill_Amount,Cust_id, Purchased_on) values({} ,{},'{}', {}, {}, {}, {}, '{}')".format(r_no, prd_no, prd_name, prd_qty ,subT , bill_amt , cust_id , pdate))
                    con.commit()
                    cur.execute("update Products set Qty_purchased = Qty_purchased + {} where Prd_id = {}".format(prd_qty, prd_no))
                    con.commit()
                    cur.execute("update Products set Available_Stock = Available_Stock - {} where Prd_id = {}".format(prd_qty, prd_no))
                    con.commit()
                    no_items = no_items-1
                    # Search for existing customer
        cur.execute("select cust_id, Cust_Name from Customers where cust_id = {}".format(cust_id))
        data = cur.fetchall()
        # Updating credit detail of existing customer
        if cur.rowcount == 1:
            cur.execute("update Customers set Monthly_credit = Monthly_credit+ {} where cust_id = {}".format(bill_amt, cust_id))
            con.commit()
        # Populating New customer info
        else:
            cur.execute("insert into Customers values({} , '{}', {}, '{}', {})".format(cust_id ,Cust_Name, Phone_No, Address, bill_amt))
            con.commit()
        print("Bought Successfully")
        # Saving bill info for each Invoice
        # Output text file path same as this prg file
        # Customer info
        print ("Generate Invoice ")
        q = 'CLOUD CAFE <3 \n\nName \t\t\t : {}\nPhone No \t\t : {}\nInvoice No \t\t : {}\nBill Amount\t\t : {}\nDate Of Purchase\t : {}\n'.format(Cust_Name.ljust(17,' '),str(Phone_No).ljust(17,' '), r_no, bill_amt, pdate)
        #1 Default file = blank text file
        filename = "Cafebill.txt"
        f=open(filename , 'w')
        f.write(q)
        # Purchase details
        cur.execute("select Prd_Name, Qty_ordered, 1.20*Sub_Total_Cost from Invoice where Receipt_no = {}".format(r_no))
        data = cur.fetchall()
        rowc = cur.rowcount
        f.write('__________________________________________\n Item\t\tQuantity\t\tCost\n__________________________________________')
        for row in data:
            f.write('\n\n {}\t\t{}\t\t{}\n'.format(str(row[0]).ljust(13,' '),row[1],row[2]))
            # Closing line
        q1 = '\n__________________________________________\n\n Thank You! Please Visit Again.'
        f.write(q1)
        f.close()
        # Renaming output file with Invoice no
        fnam = 'bill_'+str(r_no)+'_'+pdate+'.txt'
        os.rename(filename,fnam)
        print("Invoice",fnam, "generated successfully")
    except Exception as e:
        print ("Sorry for the Inconvenience",e)
		
# Sales Report
# Stock Report
def salesreport():    
    try:
        db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=db.cursor()
        print('Monthwise Revenue Collection')
        cur.execute("select distinct(month(purchased_on)) as Month, cast(sum(Total_Bill_Amount) as unsigned int) as Total_Revenue from invoice group by month(purchased_on)")
        
        try:
            with open('revenue.csv','w', newline='') as csvfile:            
                if not csvfile:
                    print("Csv not created")
                mywriter = csv.writer(csvfile)
                mywriter.writerow([i[0] for i in cur.description])
                mywriter.writerows(cur)

            with open('revenue.csv','r', newline='') as csvfile:                 
                myreader=csv.reader(csvfile,delimiter=',')                
                for rec in myreader:
                    print("%0s"%rec[0],"%40s"%rec[1])
        except:        
            print ("CSV error")
    except:
        print ("Unable to view sales")

#salesreport()

def productdetails():
    try:
        db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=db.cursor()
        print('Product Demand View')
        cur.execute("select Prd_Name as Product, Qty_purchased as Demand from products")
        try:
            with open('products.csv','w', newline='') as csvfile:            
                if not csvfile:
                    print("Csv not created")
                mywriter = csv.writer(csvfile)
                mywriter.writerow([i[0] for i in cur.description])
                mywriter.writerows(cur)

            with open('products.csv','r', newline='') as csvfile:                 
                myreader=csv.reader(csvfile,delimiter=',')                
                for rec in myreader:
                    print("%0s"%rec[0],"%40s"%rec[1])
        except:        
            print ("CSV error")
    except:
        print ("Unable to view product table")

#productdetails()

# Search for customer info
def srch_customer():
    try:
        # db=cntr.connect(host='localhost',user='root',password='Pisces',database='ProjectXII')
        cur=con.cursor()
        print('Customer Recall')
        print('1. Name search')
        print('2. Phone number search')
        print('3. Dues > INR 150')
        c = int(input("Enter your choice : "))
        if c == 1:
            CName = str(input("Enter Customer Name : "))
            cur.execute("select * from Customers where cust_name = '{}'".format(CName))
            data = cur.fetchall()
            print(data)
        elif c == 2:
            PNum = int(input("Enter Phone number : "))
            cur.execute("select * from Customers where Phone = {}".format(PNum))
            data = cur.fetchall()
            print(data)
        elif c == 3:
            print('List of Ids with credit exceeding INR 150 :')
            cur.execute("select cust_id, monthly_credit from Customers where Monthly_credit > 150")
            data = cur.fetchall()
            print(data)
        else:
            print("INVALID CHOICE")
    except:
        print ("Unable to find customer data")

##Interface Flow details
##1. First use #choice4# for register/login/exit
##2. After *login* use #choice# for stock view/customer service/exit
##3. For *stock view*, use #choice2# for stock add/view/modify/exit
##4. For *customer service*, use #choice3# for item purchase/sales report/customer search/exit
        
c = 'y'
while c.lower() == 'y' :
    print("Welcome to CLOUD CAFE !".center(89 , '='))
    print('1. Register')
    print('2. Login')
    print('3. De-register')
    print('4. Exit')
    choice4 = int(input("Enter the serial number of your choice : "))
    #Register for the 1st time
    if choice4 == 1 :
        # system("cls")
        register()
    elif choice4 == 2 :
        #system("cls")
        if login() :
            #system("cls")
            C = 'y'
            while C.lower() == 'y' :
                
                #system("cls")
                print("CLOUD CAFE".center(89 , '='))
                print("1. VIEW PANTRY ")
                print("2. CUSTOMER SERVICE")
                print("3. EXIT")
                #choice = 2
                choice = int(input("Enter your choice : "))
                if choice == 1 :
                    #system("cls")
                    print("PANTRY SURVEY".center(89 , '='))
                    print("1. Add a new Stock")
                    print("2. View all Stock")
                    print("3. Update an existing Stock")
                    print("4. Exit")
                    choice2 = int(input("Enter the choice : "))
                    if choice2 == 1 :
                        #system("cls")
                        add_prd()
                    elif choice2 == 2:
                        #system("cls")
                        view_prd()
                    elif choice2 == 3 :
                        #system("cls")
                        update_prd()
                    elif choice2 == 4 :
                        print("Goodbye")
                        break
                    else :
                        print("INVALID CHOICE")
                elif choice == 2 :
                    #system("cls")
                    print('SALES COUNTER'.center(89 , '='))
                    print('1. Prepare Customer Order')
                    print('2. View Sales this month')
                    print('3. View details about the stock')
                    print('4. Customer Details')
                    print('5. Exit')
                    choice3 = int(input("Enter your choice : "))
                    if choice3 == 1 :
                        #system("cls")
                        takeout()
                    elif choice3 == 2 :
                        #system("cls")
                        salesreport()
                    elif choice3 == 3:
                        #system("cls")
                        productdetails()
                    elif choice3 == 4 :
                        #system("cls")
                        srch_customer()
                    elif choice3 == 5 :
                        print("Goodbye")
                        break
                    else :
                        print("INVALID CHOICE")
                elif choice == 3 :
                    print("Goodbye")
                    break
                else :
                    print("INVALID CHOICE")
                    C = input("Do you want to continue (y/n) : ")
        else :
            print("Either your username or password is incorrect")
    elif choice4 == 3 :
        #system("cls")
        exStaff()
    elif choice4 == 4 :
        print("Goodbye")
        break
    else :
        print("INVALID CHOICE")
    c = input("Do you want to return to main menu (y/n) : ")
else :
    print("Goodbye")
