import sqlite3

conn = sqlite3.connect('employee.db')

c=conn.cursor()

c.execute("""create table employee (
    first text,
    last text,
    pay int
)""")