# create a sqlite3 database and table
import sqlite3 as sq
conn = sq.connect("new.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE population (city TEXT,state TEXT, population INT)""")
conn.close
