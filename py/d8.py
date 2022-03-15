import sqlite3

def muldata(dl):

    con = sqlite3.connect('st2.db')
    cursor = con.cursor()


    iq = '''INSERT INTO students
            VALUES(?,?,?,?) '''

    cursor.executemany(iq, dl)

    con.commit()
    print("no of records inserted: ",cursor.rowcount)
    con.commit()
    con.close()

dl = [(1,'raj',92,'banglore'),(2,'raju',91,'chennai'),(3,'rajesh',93,'mumbai'),(4,'martha',94,'banglore'),(5,'ulrich',90,'chennai'),(6,'jonas',89,'mumbai'),(7,'anna',97,'banglore'),(8,'hanna',96,'chennai'),(9,'charlotte',87,'mumbai'),(10,'thomas',79,'banglore')]

muldata(dl)

