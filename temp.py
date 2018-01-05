import sqlite3 as sq
with sq.connect("new.db") as connection:
    c = connection.cursor()
    pops = [("delhi","delhi",12345),("sidhi","MP",12121212)]
    try:
        c.executemany("INSERT INTO population VALUES(?,?,?)",pops)
    except sq.OperationalError:
        print("oops something is wrong")