import sqlite3
con = sqlite3.connect('st2.db')

cursor = con.cursor()

sqlit = '''SELECT * FROM students ORDER BY marks DESC
            '''

cursor.execute(sqlit)

records = cursor.fetchall()
print(records)

for row in records:
    print('id:', row[0])
    print('name:', row[1])
    print('marks:', row[2])

con.commit()
con.close()

