import pymysql

db= pymysql.connect(host="localhost",user="root",password="venisha",database="pythondb")

cursor =db.cursor()

sql = "SELECT * FROM EMPLOYEE \
      WHERE INCOME > '%d'" % (1000)
try:

    cursor.execute(sql)

    #fetch all the rows in a lists of lists
    results=cursor.fetchall()
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
        # Now print fetched result

        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d"%\
            (fname,lname,age,income))
except:
    print("Error: unable to fetch data")

#disconnect from server
db.close()

