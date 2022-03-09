import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='bruhh',database='electronic_shop')
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()
c1.execute("CREATE TABLE employee(emp_code int(4)primary key ,emp_name varchar(25) ,password int(8)not null,purchased bigint)")
print("EMPLOYEE table created")
c1.execute("create table elect(Product_name varchar(55),Product_no bigint primary key,Stock varchar(10),Price_per varchar(1000))")
print("electronic items table created")
c1.execute("create table users(user_code int(4) primary key,user_name varchar(25),password int(8)not null,city varchar(25),ph_no bigint)")
print("users table created")


           

            