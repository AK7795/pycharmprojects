import sqlite3


con = sqlite3.connect('em2.db')
cursor = con.cursor()

sqlit = "SELECT * FROM employees ORDER BY name"

cursor.execute(sqlit)

rec = cursor.fetchall()
print(rec)

for i in rec:
    print('empcode  :', i[0])
    print('name:', i[1])
    print('phone :',i[2])
    print('email :', i[3])
    print('designation :', i[4])
    print('salary :', i[5])
    print('company name :', i[6])
con.commit()
con.close()

