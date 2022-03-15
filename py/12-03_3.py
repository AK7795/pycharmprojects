import sqlite3

def data(dl2):

    con = sqlite3.connect('cus.db')
    cursor = con.cursor()


    ins = '''INSERT INTO customer_details
            VALUES (?,?,?,?) '''

    cursor.executemany(ins, dl2)

    con.commit()
    print("no of records inserted: ",cursor.rowcount)
    con.commit()
    con.close()

dl2 = [(10,'thomas','kolkata',3)]

data(dl2)

