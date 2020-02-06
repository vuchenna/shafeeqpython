import pymysql as mysql
db = mysql.connect("localhost", "root", "", "QA")

c= db.cursor()
c.execute("insert into school values(24,'peter','maths', 750)")
db.commit()