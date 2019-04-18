import sqlite3



def create_db():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS people(id INTEGER PRIMARY KEY AUTOINCREMENT,he TEXT,she TEXT,contract TEXT)")
    con.close()

def load_db():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM people")
    list = cursor.fetchall()
    return list

def insert(data):
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    try:
        cursor.execute("INSERT INTO people (he, she, contract) VALUES(?,?,?)",data)
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    con.commit()
    con.close()

def delete(id):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    try:
        cur.execute('DELETE FROM people WHERE id=?',id)
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    con.commit()
    con.close()
