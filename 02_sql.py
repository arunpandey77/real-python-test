import sqlite3 as sq
conn = sq.connect("new.db")
cursor = conn.cursor()
cursor.execute("""INSERT INTO population VALUES('san francisco','NY',840000)""")
cursor.execute("""INSERT INTO population VALUES('jabalpur','MP',900000)""")
conn.commit()
conn.close()