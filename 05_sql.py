import sqlite3 as sq
import random
with sq.connect("new.db") as con:
    c = con.cursor()
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int)")
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))