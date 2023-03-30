import pymysql

db= pymysql.connect(host="localhost",user="root",password="venisha",database="pythondb")

cursor =db.cursor()

#prepare SQL query to INSERT a record into the database
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,
    LAST_NAME,SEX,INCOME)
    VALUES('Mac','Mohan',20,'M',2000)"""# Selection sort in Python.py"""

try:
    cursor.execute(sql)
    db.commit()

except:
    db.rollback()

db.close()