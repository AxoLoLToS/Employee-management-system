import mysql.connector as a
conn=a.connect(host='localhost',user='root',passwd='bruhh',database='emptable')

def nperson():
    ecode=input('Enter Employee Code: ')
    name=input('Enter Employee Name: ')
    post=input('Enter Employee Post: ')
    join=input('Enter Employee Joining Date: ')
    salary=input('Enter Employee Salary: ')
    sql='''INSERT INTO office VALUES(%s,%s,%s,%s,%s);'''
    c=conn.cursor()
    c.execute(sql,(ecode,name,post,join,salary))
    conn.commit()
    print('Employee Data Added Successfully')
    main()
    
def person():
    sql="select * from personal;"
    c=conn.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()
    
def noffice():
    ec=input('Enter Employee Code: ')
    n=input('Enter Employee Name: ')
    ps=input('Enter Employee Dept: ')
    j=input('Enter Employee Joining Date: ')
    sal=input('Enter Employee Salary: ')
    data=(ec,n,ps,j,sal)
    sql="insert into office values(%s,%s,%s,%s,%s);"
    c=conn.cursor()
    c.execute(sql,data)
    conn.commit()
    print('Employee Data Added Successfully')
    main()
    
def office():
    sql="select * from office"
    c=conn.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()
    
def nsalary():
    ecode=input('Enter Employee Code: ')
    name=input('Enter Employee Name: ')
    post=input('Enter Employee Post: ')
    join=input('Enter Employee Joining Date: ')
    salary=input('Enter Employee Salary: ')
    sql='''INSERT INTO salary VALUES(%s,%s,%s,%s);'''
    c=conn.cursor()
    c.execute(sql,(ecode,name,post,join,salary))
    conn.commit()
    print('Employee Data Added Successfully')
    main()

def salary():
    sql="select * from salary"
    c=conn.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()
    
def main():
    print('1.Add Employee Data')
    print('2.View Employee Data')
    print('3.Add Employee Details')
    print('4.View Employee Details')
    print('5.Add Salary Details')
    print('6.View Salary Details')
    print('7.Exit')
    ch=int(input('Enter your choice(1-7): '))
    while True:
        if ch==1:
            nperson()
        elif ch==2:
            person()
        elif ch==3:
            noffice()
        elif ch==4:
            office()
        elif ch==5:
            nsalary()
        elif ch==6:
            salary()
        elif ch==7:
            print('Thank You')
            break
        else:
            print('Invalid Choice')
main()
