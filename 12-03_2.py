import sqlite3
con = sqlite3.connect('cus.db')
cursor = con.cursor()
sqlit = '''SELECT * FROM customer_details
            WHERE id = 2
            '''

cursor.execute(sqlit)

rec = cursor.fetchall()
print(rec)

for i in rec:
    print('id:', i[0])
    print('name:', i[1])
    print('city :',i[2])
    print('no of tickets:', i[3])

con.commit()
con.close()

