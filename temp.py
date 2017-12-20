import sqlite3 as sq
conn = sq.connect("cars.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE INVENTORY(make TEXT, model TEXT, quantity INT)""")
conn.close()