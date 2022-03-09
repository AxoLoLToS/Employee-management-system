import mysql.connector
import random

conn = mysql.connector.connect(host='localhost', username='root',password='root', database='carnival')
my_cursor = conn.cursor()

print("\n********************WELCOME TO CARNIVAL CINEMAS TICKET BOOKING SYSTEM***********************")

acc = input("\nDO YOU HAVE AN ACCOUNT? (Y/N):")
em = []
if acc=='y' or acc=='yes' or acc=='Y' or acc=='YES':
    email = input("\nENTER YOUR EMAIL ID:-")
    em.append(email)
    pas = input("\nENTER YOUR PASSWORD:-")
    otp = int(input("\nENTER THE OTP CODE SENT TO YOUR EMAIL AND PHONE NO:-"))
   
    print("\n-------LOGIN SUCCESSFUL-------")

else:
    nam = input("\nENTER YOUR FULL NAME:-")
    pn = int(input("\nENTER YOUR PHONE NO:-"))
    city = input("\nENTER YOUR CITY NAME:-")
    state = input("\nENTER YOUR STATE:-")
    email = input("\nENTER YOUR EMAIL ID:-")
    em.append(email)
    passw = input("\nENTER YOUR PASSWORD:-")
    print(f"\nOTP SENT TO {pn} AND {em}")
    ot = int(input("\nENTER THE OTP NO:-"))
    
    print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")

print("\n NOW SHOWING----")
query1 = "select movies from movies"
my_cursor.execute(query1)
for a in my_cursor:
    print(a)

name = []
mname = input("\n WHICH MOVIE DO YOU WANT TO WATCH :-")
tik = int(input("\n ENTER THE NUMBER OF TICKETS YOU WANT :-"))
for b in range(tik):
    nam = input("\nENTER NAME :-")
    name.append(nam)

hall = []
date = []
time = []
charges = []
query2 = "select hall from movies where movies = '{}' ".format(mname)
my_cursor.execute(query2)
for c in my_cursor:
    hall.append(c)

query3 = "select date from movies where movies = '{}'".format(mname)
my_cursor.execute(query3)
for d in my_cursor:
    date.append(d)

query4  = "select time from movies where movies = '{}'".format(mname)
my_cursor.execute(query4)
for e in my_cursor:
    time.append(e)

query5 = "select charges*{} from movies where movies = '{}'".format(tik, mname)
my_cursor.execute(query5)
for f in my_cursor:
    charges.append(f)

seatnum = random.randint(1, 100)


print(f"YOU HAVE TO PAY {charges} RUPEES")
pay = input("TO PAY ENTER (P) :-")

print("\nYour ticket is here - ")

if tik==1:
    print(f"\nNAME = {name}          MOVIE NAME = {mname}      HALL = {hall}")
    print(f"TIME = {time}      DATE = {date}             CHARGES = {charges}      ")
    print(f"seat number = {seatnum}")
    print(f"Your ticket has been sent to your email {em}")

if tik>1:
    print(f"\nNAME = {name}          MOVIE NAME = {mname}      HALL = {hall}")
    print(f"TIME = {time}      DATE = {date}             CHARGES = {charges}      ")
    print(f"seat number = {seatnum} to {seatnum+(tik-1)}")
    print(f"Your ticket has been sent to your email {em}")



conn.close()