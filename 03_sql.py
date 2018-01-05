import sqlite3 as sq
with sq.connect("new.db") as connection:
	c = connection.cursor()
	city = [('bhopal','mp',5000000),('indore','mp',2309302302),('bangalore','ka',23232309)]
	c.executemany('INSERT INTO population VALUES(?,?,?)',city)