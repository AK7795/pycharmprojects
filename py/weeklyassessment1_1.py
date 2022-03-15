import sqlite3

con = sqlite3.connect('em2.db')

cursor = con.cursor()

sq = '''CREATE TABLE employees (
    empCode INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT,
    designation TEXT,
    salary REAL,
    companyName TEXT)'''

cursor.execute(sq)

print('table is created successfully')

con.commit()
con.close()

