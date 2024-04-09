from tkinter import *
import mysql.connector as mysql
import sys

def submitcom(): #takes the username and password from the form
    user=userValue.get()
    passw=passValue.get()
    loginDBMS(user,passw)
    
def loginDBMS(user,passw):
    Ruser,Rpassw="madhav","12345"

    if (Ruser,Rpassw)==(user,passw):
        MsgLabel=Label(frameLog,text="Login Successful!!",bg="#e900f4",fg="#292629",font="Times 15 bold")
        MsgLabel.place(x=30,y=260,height=40,width=200)

        db=mysql.connect(user="root",password="8447",host="localhost",database="medicines",port="33061")
        cursor=db.cursor()

        saveQuery="SELECT * FROM STOCK"

        try:
            cursor.execute(saveQuery)
            records=cursor.fetchall()

            #Displaying the stock records
            for i in records:
                print(i)
                
            sys.stderr.write("Query Executed Successfully!!")    

        except:
            db.rollback()
            sys.stderr.write("Error Occurred")

    else:
        MsgLabel=Label(frameLog,text="Incorrect Username or Password\nLogin Failed!!",bg="#e900f4",fg="#292629",font="Times 15 bold")
        MsgLabel.place(x=30,y=260,height=60,width=280)


root = Tk()
root.geometry("640x360")
root.title("DBMS Login Page")
  
 
# Making Frame1 for Image

frameImage=Frame(root)
frameImage.pack(side=LEFT,fill="y")

photo=PhotoImage(file="image.jpg")
imageLabel=Label(frameImage,image=photo).pack()


#Making Frame2 for Login
frameLog=Frame(root,bg="#02cfec",width="320")
frameLog.pack(side=RIGHT,fill="y")

userLabel=Label(frameLog,text="Username - ",bg="#2dfa43",fg="#570bdc",font="Times 15 bold")
passLabel=Label(frameLog,text="Password - ",bg="#2dfa43",fg="#570bdc",font="Times 15 bold")
headLabel=Label(frameLog,text="Login",bg="#02cfec",fg="#1e4045",font="Times 25 bold underline")

userLabel.place(x=30,y=90,height=30,width=120)
passLabel.place(x=30,y=150,height=30,width=120)
headLabel.place(x=30,y=40)

userValue=StringVar()
passValue=StringVar()

userEntry=Entry(frameLog,textvariable=userValue).place(x=160,y=90,height=30)
passEntry=Entry(frameLog,textvariable=passValue,show="*").place(x=160,y=150,height=30)

#Submit Button
buttonLog=Button(frameLog,text="Login",command=submitcom,bg="#ff0202",font="Times 15").place(x=160,y=200,height=30,width=70)


root.mainloop()




print()
print("*************************************************************")
sys.stderr.write(       "         MEDICAL STORE MANAGEMENT SYSTEM \n")
print("*************************************************************")
print()
print()
print("         1. About the project")
print("         2. Display list of all medicines available in the stock")
print("         3. Display all medicines in alphabetical order")
print("         4. Add new medicines purchases in stock table")
print("         5. Update price of medicine")
print("         6. Delete a medicine detail from table stock if not available")
print("         7. Show details of all sales done from the table bill")
print("         8. Enter all customers orders and maintain record")
print("         9. Total bill to be paid - Customerwise")
print("         10. Total medicines bought according to mobile number (Group by)")


def about():
  print('''You are welcome to MEDICAL STORE MANAGMENT project . It has 12 choices. It has used 2 Tables  named as  Stock and Bill.
        We also offer 10% discount on all the medicines''')

db=mysql.connect(user='root',password='8447',host='localhost',database='medicines',port="33061")
cursor=db.cursor()

def showlist():
  print('Display all details of medicines available')
  print()
  myquery1="select * from stock"
  cursor.execute(myquery1)
  records=cursor.fetchall()
  for i in range(0,cursor.rowcount):
    print(records[i],"\n")


def sort_medicines():
    print('sorting medicines names in ascending order')
    print()
    myquery1="select* from stock order by description"
    cursor.execute(myquery1)
    records=cursor.fetchall()
    for i in range(0,cursor.rowcount):
        print(records[i],"\n")

def add_stock():
    print('Adding new medicine in the stock')
    myquery="select * from stock"
    cursor.execute(myquery)
    records=cursor.fetchall()
    for i in range(0,cursor.rowcount):
        print(records[i],"\n")
    L=[]
    mcode=input("Enter Medicine Code to be added")
    L.append(mcode)
    mname=input("Enter Medicine name")
    L.append(mname)
    dateofexp=input("Enter date of expiry")
    L.append(dateofexp)
    price=input("Enter Medicine price")
    L.append(price)
    quantity=input("Enter Medicine quantity")
    L.append(quantity)
    record=L
    command="insert into stock(m_code,description,expiry_date , price , quantity) values(%s,%s,%s,%s,%s)"
    cursor.execute(command,record)
    db.commit()
    print("record inserted") 
    myquery="select * from stock"
    cursor.execute(myquery)
    records=cursor.fetchall()
    for i in range(0,cursor.rowcount):
        print(records[i],"\n")

def update_stock():
    print("change the price of medicine")
    print("old prices")
    myquery1="select * from stock"
    cursor.execute(myquery1)
    records=cursor.fetchall()
    for i in range(0,cursor.rowcount):
        print(records[i],"\n")
    m=int(input('Enter the medicine code for which price is to be increased'))
    update=float(input('Enter the new price for the medicine'))
    myquery2="update stock set price=%s where m_code =%s"%(update,m)
    cursor.execute(myquery2)
    db.commit()
    print("prices increased")
    print("updated data")
    myquery3="select * from stock"
    cursor.execute(myquery3)
    records=cursor.fetchall()
    for i in range(0,cursor.rowcount):
        print(records[i],"\n")

def delete_stock():
    print("Before any changes in stock")
    print()
    myquery1="select * from stock"
    cursor.execute(myquery1)
    records=cursor.fetchall()
    for i in range(0,cursor.rowcount):
        print(records[i],"\n")
    m=int(input('Enter the medicine code to be deleted'))
    myquery2="delete from stock where m_code=%s"%(m,)
    cursor.execute(myquery2)
    print("record deleted successfully")
    print("Table after the record deletion")
    myquery3="select * from stock"
    cursor.execute(myquery3)
    records=cursor.fetchall()
    for i in range(0,cursor.rowcount):
        print(records[i],"\n")

def bill_records():
    print("billing maintainance table:")
    print()
    myquery1="select * from billing"
    cursor.execute(myquery1)
    records=cursor.fetchall()
    for i in range(0,cursor.rowcount):
        print(records[i],"\n")

def record_orders():
  import datetime
  print('Following is the list and price of medicines')
  myquery1="select * from stock"
  cursor.execute(myquery1)
  records=cursor.fetchall()
  for i in range(0,cursor.rowcount):
      print(records[i],"\n")
  L=[]
  mob_no=int(input('Please enter your mobile no.'))
  L.append(mob_no)
  bill_no=int(input('Enter bill no')) 
  L.append(bill_no)
  date=datetime.datetime.now()
  d=date.strftime('%Y-%m-%d')
  L.append(d)
  m_code=int(input('Enter medicine code'))
  m=m_code
  q2='select* from stock where m_code= %s'%(m,)
  cursor.execute(q2)
  d=cursor.fetchall()
  if d==[]:
      print('Sorry! Medicine not available')
  else:    
      L.append(m_code)
      m_name='select description from stock where m_code=%s'%(m,)
      cursor.execute(m_name)
      d=cursor.fetchall()
      p=str(d[0][0])
      L.append(p)
      q='select quantity from stock where m_code=%s'%(m,)
      cursor.execute(q)
      d=cursor.fetchall()
      p=int(d[0][0])
      print('Quantity of medicine available:',p)
      quantity=int(input('Enter quantity of medicine'))
      if quantity>p:
          print('This much quantity is not available')
      else:
          L.append(quantity)
          A=[p,quantity,m]
          update='update stock set quantity=%s-%s where m_code=%s'
          cursor.execute(update,A)
          price='select price from stock where m_code=%s'%(m,)
          d=cursor.execute(price)
          a=cursor.fetchall()
          p=float(a[0][0])
          L.append(p)
          discount=0.1*p*quantity
          L.append(discount)
          total=p*quantity-discount
          L.append(total)
          record=L
          command="insert into billing(mobile_no,bill_no,date_of_purchase,med_code,med_name,quantity,mrp,discount,total_price)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          cursor.execute(command,record)
          db.commit()
          print('record inserted')
          myquery1="select * from billing"
          cursor.execute(myquery1)
          records=cursor.fetchall()
          for i in range(0,cursor.rowcount):
              print(records[i],"\n")



def sum_bill_by_cust():
  myquery1="select * from stock"
  cursor.execute(myquery1)
  records=cursor.fetchall()
  for i in range(0,cursor.rowcount):
      print(records[i],"\n")
  print("Sum of price of all medicines purchased by the customer")
  mob=int(input('Enter mobile no.:'))
  query='select med_name, quantity, mrp from billing where mobile_no=%s;'%(mob,)
  cursor.execute(query)
  records=cursor.fetchall()
  for i in range(0,cursor.rowcount):
      print(records[i],'\n')
  print('you total bill to pay is')
  command='select sum(quantity*mrp) as "your total bill as of now is" from billing where mobile_no=%s;'%(mob,)
  cursor.execute(command)
  records=cursor.fetchall()
  p=records[0][0]
  print(p)


def groupby():
 code=int(input('Enter the medicine code for checking of sale'))
 print('total quantity of the selected sold along with its code  and name')
 cursor.execute('select sum(quantity), med_name from billing where med_code=%s '%(code,))
 for i in cursor:
     print(i)


# handler of entire program
ans="Yes"
while ans=='Yes':
    opt=int(input("Enter your choice:"))
    if opt==1:
        about()
    elif opt==2:
        showlist()
    elif opt==3:
        sort_medicines()
    elif opt==4:
        add_stock()
    elif opt==5:
        update_stock()
    elif opt==6:
        delete_stock()
    elif opt==7:
        bill_records()
    elif opt==8:
        record_orders()
    elif opt==9:
        sum_bill_by_cust()
    elif opt==10:
        groupby()
    print()  
    ans=input('''Want more information?
              Reply with Y or N:''')
    if ans=="Y":
        ans='Yes'
    else:
        break
