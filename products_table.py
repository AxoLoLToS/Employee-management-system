import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='bruhh',database='electronic_shop')
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()
c1.execute("insert into elect values ('Switch',123456,'81','50')")
c1.execute("insert into elect values ('mouse',456789,'45','650')")
c1.execute("insert into elect values ('Water motor',623455,'20','15000')")
c1.execute("insert into elect values ('Hammer',645124,'198','250')")
c1.execute("insert into elect values ('Screw',645224,'4000','15')")
c1.execute("insert into elect values ('Wire(in m)',647123,'100','200')")
c1.execute("insert into elect values ('Switch board',647124,'200','150')")
c1.execute("insert into elect values ('Land motor',698655,'25','10000')")
conn.commit()
print ("updated  successfully")

