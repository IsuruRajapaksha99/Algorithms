import pymysql

db= pymysql.connect(host="localhost",user="root",password="venisha",database="pythondb")

cursor =db.cursor()

#Drop table if it already exist using execute() method
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Create table as per requirement
sql="""CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)"""

cursor.execute(sql)

db.close()