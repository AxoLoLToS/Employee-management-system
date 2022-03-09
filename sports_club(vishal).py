import os
import platform
import mysql.connector  
conn=mysql.connector.connect(host="localhost",user="root",passwd="bruhh",database="sportsclub")
if conn.is_connected():
        print('successfully connected')
mycursor=conn.cursor()
print('welcome to the sports club management system')

def MenuSet():
    print('1.Register a club member')
    print('2.View club members')
    print('3.Search club member')
    print('4.Remove club member')
    print('5.Exit')
    ch=int(input('enter your choice:'))
    if ch==1:
        RegisterClub()
    elif ch==2:
        ClubView()
    elif ch==3:
        SearchClub()
    elif ch==4:
        RemoveClub()
    elif ch==5:
        exit()
    else:
        print('enter a valid choice')

def runAgain():
    runagn=input('do you want to run the program again?(y/n):')
    if (runagn.lower()=='y'):
        MenuSet()
    if(platform.system()=='Windows'):
        print(os.system('cls'))
    else:
        print(os.system('clear'))
        MenuSet()

def RegisterClub():
    l=[]
    enroll=int(input('enter your registration number:'))
    l.append(enroll)
    sname=input('enter your club name:')
    l.append(sname)
    age=int(input('enter age of member:'))
    l.append(age)
    city=input('enter city of the member:')
    l.append(city)
    sport=input('enter sport of the member:')
    l.append(sport)
    regfee=int(input('enter registration fee:'))
    l.append(regfee)
    value=l
    sql='insert into sportsclub values(enroll,sname,age,city,sport,regfee) values(%s,%s,%s,%s,%s,%s)' 
    mycursor.execute(sql,value)
    mydb.commit()
    
def ClubView():
    print('select the search criteria')
    print('1.enroll')
    print('2.sname')
    print('3.age')
    print('4.city')
    print('5.address')
    print('6.all')
    ch=int(input('enter your choice:'))
    if ch==1:
        s=int(input('enter enroll:'))
        rl=(s,)
        sql='select * from sportsclub where enroll=%s'
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input('enter sname:')
        rl=(s,)
        sql='select * from sportsclub where sname=%s'
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input('enter age:'))
        rl=(s,)
        sql='select * from sportsclub where age=%s'
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input('enter city:')
        rl=(s,)
        sql='select * from sportsclub where city=%s'
        mycursor.execute(sql,rl)
    elif ch==5:
        s=input('enter address:')
        rl=(s,)
        sql='select * from sportsclub where address=%s'
        mycursor.execute(sql,rl)
    elif ch==6:
        sql='select * from sportsclub'
        mycursor.execute(sql)
        
    result=mycursor.fetchall()
    print('the members of the club are:')
    print('(enroll,sname,age,city,sport)')
    for x in result:
        print(x)
        
def SearchClub():
    print('please enter the details to view the fee details-')
    enroll=int(input('enter the enroll number of the member whose fee is to be viewed:'))
    rl=(enroll,)
    sql='select * from sportsclub where enroll=%s'
    mycursor.execute(sql,rl)
    
    result=mycursor.fetchall()
    if result==None:
        print('no such member found')
        return
        print('the details of the member are:')
    
    for x in result:
        print(x)
        
def RemoveClub():
    print('please enter the details to remove the member-')
    enroll=int(input('enter the enroll number of the member to be removed:'))
    rl=(enroll,)
    sql='delete from sportsclub where enroll=%s'
    mycursor.execute(sql,rl)
    mydb.commit()

MenuSet()
runAgain()
