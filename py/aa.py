import sqlite3

con = sqlite3.connect('st2.db')

cursor = con.cursor()
sq = '''CREATE TABLE students(
               id INTEGER PRIMARY KEY,
               name TEXT ,
               marks INTEGER,
               city TEXT)'''

cursor.execute(sq)

print('table is created successfully')

con.commit()
con.close()

