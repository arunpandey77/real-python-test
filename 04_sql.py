import sqlite3 as sq
import csv
with sq.connect("new.db") as connection:
    c = connection.cursor()
    employees = csv.reader(open("employees.csv","rU"))
    c.execute("CREATE TABLE employees(firstname TEXT,lastname TEXT)")
    c.executemany("INSERT INTO employees values(?,?)",employees) 
