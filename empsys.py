# Project on Employee Management System
import mariadb as driver
import sys

#Final program loop
def menu():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print("........MENU.......")
        print("1. CREATE DATABASE")
        print("2. SHOW DATABASES")
        print("3. CREATE TABLE")
        print("4. SHOW TABLES")
        print("5. INSERT RECORD")
        print("6. UPDATE RECORD")
        print("7. DELETE RECORD")
        print("8. SEARCH RECORD")
        print("9. DISPLAY RECORD")
        print()
        print()
        choice=int(input("Enter the choice (1-9) : "))
        if(choice==1):
            create_database()
        elif(choice==2):
            show_databases()
        elif(choice==3):
            create_table()
        elif(choice==4):
            show_tables()
        elif(choice==5):
            insert_record()
        elif(choice==6):
            update_record()
        elif(choice==7):
            delete_record()
        elif(choice==8):
            search_record()
        elif(choice==9):
            display_record()
        else:
            print("Wrong Choice.")
        loop=input("Do you want more try? Press 'y' to continue...")
    else:
        sys.exit()

#Creates databse 'employee' if it doesn't exist       
def create_database():
    con=driver.connect(host='localhost',user='root', passwd='$tr0ngp@$$w0rd')
    
    cur=con.cursor()
    cur.execute('create database if not exists employee')
    print()
    print("Database Created")
    con.close()

#Shows databases in computer
def show_databases():
    con=driver.connect(host='localhost',user='root',passwd='$tr0ngp@$$w0rd')
    
    cur=con.cursor()
    cur.execute('show databases')
    for i in cur:
        print(i)
    con.close()

#In order to create a new table, if it doesn't exist  
def create_table():
    con=driver.connect(host='localhost',user='root',passwd='$tr0ngp@$$w0rd',database='employee')
    
    cur=con.cursor()
    cur.execute('create table if not exists emp(ID integer primary key, ENAME varchar(15), SALARY float, POSITION varchar(25), AGE int(3))')
    print()
    print("Table Created -> EMP")
    cur.execute('DESC emp')
    print("+-------------|--------------|-----------+")
    print("+Column Name  |DataType(Size)|NULL       |")
    print("+-------------|--------------|-----------+")
    for i in cur:
        print(f"|{i[0]} | {i[1]} | {i[2]}| {i[3]}| {i[4]}|")
    print("+-------------|--------------|-----------+")
    con.close()

#Its function is to show all the tables present in the database
def show_tables():
    con=driver.connect(host='localhost',user='root',passwd='$tr0ngp@$$w0rd',database='employee')
    
    cur=con.cursor()
    cur.execute('show tables')
    for i in cur:
        print(i)
    con.close()

#Inserts employee records
def insert_record():
    con=driver.connect(host='localhost',user='root',passwd='$tr0ngp@$$w0rd',database='employee')        #print("Successfully Connected")
    cur=con.cursor()
    ID=int(input("ENTER EMPLOYEE ID : "))
    NAME=input("ENTER NAME OF EMPLOYEE : ")
    SALARY=float(input("ENTER EMPLOYEE SALARY : "))
    POSITION=input("ENTER EMPLOYEE POSITION : ")
    AGE=float(input("ENTER EMPLOYEE AGE : "))
    query1="INSERT INTO emp(id,ename,salary,position,age) VALUES({},'{}',{},'{}',{})".format(ID,NAME,SALARY,POSITION,AGE)
    cur.execute(query1)
    con.commit()
    print('Record Inserted')
    con.close()
    
    
#Updates employee records 
def update_record():
    con=driver.connect(host='localhost',user='root',passwd='$tr0ngp@$$w0rd',database='employee')
    cur=con.cursor()
    d=int(input("Enter Employee ID for update record : "))
    ID=int(input("ENTER NEW EMPLOYEE ID : "))
    name=input("ENTER NEW NAME OF EMPLOYEE : ")
    salary=float(input("ENTER NEW SALARY FOR EMPLOYEE : "))
    position=input("ENTER NEW POSITION FOR EMPLOYEE : ")
    age=float(input("ENTER NEW AGE FOR EMPLOYEE : "))
    query1="update emp set id=%s, ename='%s', salary=%s, position='%s', age=%s where id=%s" %(ID,name,salary,position,age,d)
    cur.execute(query1)
    con.commit()
    print("Record Updated")
    con.close()

#Deletes an employee's record
def delete_record():
    con=driver.connect(host='localhost',user='root',passwd='$tr0ngp@$$w0rd',database='employee')
    cur=con.cursor()
    d=int(input("Enter Employee ID for deleting record : "))
    query1="delete from emp where id={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

#Searches for an employee's record
def search_record():
    con=driver.connect(host='localhost',user='root',passwd='$tr0ngp@$$w0rd',database='employee')
    cur=con.cursor()
    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO SEARCH RECORD: ")
    print("1. ACCORDING TO ID")
    print("2. ACCORDING TO NAME")
    print("3. ACCORDING TO SALARY")
    print()
    choice=int(input("ENTER THE CHOICE (1-3) : "))
    if choice==1:
          d=int(input("Enter Employee ID which you want to search : "))
          query1="select * from emp where id=%s" %(d)
    elif choice==2:
          name=input("Enter Employee Name which you want to search : ")
          query1="select * from emp where ename='%s'" %(name)
    elif choice==3:
          sal=float(input("Enter Employee Salary which you want to search : "))
          query1="select * from emp where salary=%s" %(sal)
    else:
          print("Wrong Choice")
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    for i in rec:
        print(i)
    print("Record Searched")
    con.close()

#Shows employee records for the current table/database
def display_record():
    con=driver.connect(host='localhost',user='root',passwd='$tr0ngp@$$w0rd',database='employee')
    #print("Successfully Connected")
    cur=con.cursor()
    cur.execute('select * from emp')
    rec=cur.fetchall()
    count=cur.rowcount
    print("+----------|--------------|-----------|-----------|-----------+")
    print("+  Emp ID  |   Emp Name   |   Salary  |  Position |    Age    +")
    print("+----------|--------------|-----------|-----------|-----------+")
    for i in rec:
        print(f'|{i[0]}     | {i[1]}    | {i[2]}   |    {i[3]} |   {i[4]} |') 
    print("+----------|--------------|-----------+")
    print("+   Total no. of records are : ",count,"    |")
    print("+-------------------------------------+")
    #for i in rec:
    #    print(i)
    con.close()
    
    
menu()







