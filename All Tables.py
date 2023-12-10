import sys
import mysql.connector as sql

con = sql.connect(user="root" , password = "Pisces")

cursor= con.cursor()

#Create Database
cursor.execute("create database if not exists ProjectXII ")
cursor.execute("use ProjectXII")

#Staff Table
cursor.execute("create table if not exists Staff (Username varchar(225), Password varchar(225))")

#Product Table
cursor.execute("create table if not exists Products (Prd_id int primary key, Prd_Name varchar(255), Cost_per_piece float, Available_Stock bigint, Qty_purchased int )")

#Customer Table
cursor.execute("create table if not exists Customers (Cust_id int primary key, Cust_Name varchar(255), Phone bigint, Address varchar(255) , Monthly_credit float )")

#Invoice Table
cursor.execute("create table if not exists Invoice \
                (Invoice_id int auto_increment primary key, \
                 Receipt_no int, \
                 Purchased_on date, \
                 Prd_Name varchar(255), \
                 Qty_ordered bigint, \
                 Sub_Total_Cost float, \
                 Total_Bill_Amount float, \
                 Cust_id int, \
                 Prd_id int, \
                 foreign key(Prd_id) references products(Prd_id))")

#Add second foreign key to invoice table
#cursor.execute("alter table invoice add constraint fk_prd foreign key(Cust_id) references customers(Cust_id)")
               

print("Database and Tables created successfully")

con.close()
