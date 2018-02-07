import pymysql
db= pymysql.connect(host="localhost",user="root",password="root",database="python" )
mycursor = db.cursor()
mycursor.execute("SHOW TABLES")
print(mycursor.fetchall())
mycursor.execute("SHOW VARIABLES LIKE '%version%'")
print(mycursor.fetchall())



#-----------------------------------------------------------------------
#CREATING DATABASE PYTHON
mycursor.execute("CREATE DATABASE demopy")
mycursor.execute("USE demopy")
mycursor.execute("""CREATE TABLE customer(id int primary key,name varchar(30),email varchar(30),city varchar(25),age int,gender char(1),last_visit date)""")
mycursor.execute("SHOW TABLES")
print(mycursor.fetchall())


#--------------------------------------------------------

#INSERTING DATA INTO DATABASE "PYTHON"
mycursor.execute("""INSERT INTO customer VALUES
    (1,'Jack','jack@gmail.com','London',25,'F','2014-02-17')""")

mycursor.execute("""INSERT INTO customer VALUES
    (2,'John','john@gmail.com','Chicago',23,'F','2015-03-17')""")

mycursor.execute("""INSERT INTO customer VALUES
    (3,'James','james@gmail.com','US',26,'M','2013-04-17')""")

#  To save the changes into database:
db.commit()
mycursor.execute("SELECT * FROM customer")
print(mycursor.fetchall()) 
#-------------------------------------------------------------------------

#UPDATION OF DATA INTO DATABASE "PYTHON"
mycursor.execute("UPDATE customer SET age=24 WHERE id=1")
db.commit()
mycursor.execute("SELECT * FROM customer")
print(mycursor.fetchall()) 
mycursor.execute("DELETE FROM customer WHERE id=3")
db.commit()

db.close()
    
