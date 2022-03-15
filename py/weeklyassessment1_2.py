import sqlite3


def data(dat):

    con = sqlite3.connect('em2.db')
    cursor = con.cursor()

    inser = '''INSERT INTO employees
            VALUES (?,?,?,?,?,?,?) '''

    cursor.executemany(inser, dat)

    con.commit()
    print("no of records inserted: ",cursor.rowcount)
    con.commit()
    con.close()


dat = [(1,'john',9999888822,'johnmayer@gmail.com','associate engineer',45000,'iprimed'),(2,'tom harold',888899922,'tomshelby@gmail.com','associate engineer',49000,'iprimed'),(3,'arthur',9090909090,'arthuershelby@gmail.com','software engineer',55000,'iprimed'),(4,'robert',7987897897,'robertstark@gmail.com','associate engineer',60000,'harman'),(5,'arya',2582582693,'aryastark@gmail.com','software engineer',75000,'harman'),(6,'sophie',7475747680,'sophieturner@yahoo.com','senior associate engineer',90000,'harman'),(7,'ned',1234567890,'nedstark@gmail.com','associate engineer',76000,'iprimed')]

data(dat)

