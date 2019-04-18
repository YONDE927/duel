import sqlite3


con = sqlite3.connect('data.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM people")
list = cursor.fetchall()
print(list)
