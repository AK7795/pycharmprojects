''' Write a Program for Customer Management:
Create a Customerdetails ⇒ id,name,city,tickets
Options :
       1.viewing the customer based on customer id
       2. Total count of tickets sold
       3. City wise ticket sold
       4. Information ⇒ based on descending order
       5. Update ⇒ customer id ⇒ which detail
       6. Delete ⇒ customer id ⇒ delete the record '''

import sqlite3

con = sqlite3.connect('cus.db')

cursor = con.cursor()
sq = '''CREATE TABLE customer_details(
               id INTEGER PRIMARY KEY,
               name TEXT , 
               city TEXT,
               tickets INTEGER)'''

cursor.execute(sq)

print('table is created successfully')

con.commit()
con.close()

