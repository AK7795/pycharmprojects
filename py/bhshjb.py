import sqlite3


def show():

    c = sqlite3.connect('cus.db')

    cur = c.cursor()

    cur.execute("  FROM customer_details WHERE id = 10")

    rec = cur.fetchall()
    print(rec)

    for i in rec:
        print(i)
    c.commit()
    c.close()

