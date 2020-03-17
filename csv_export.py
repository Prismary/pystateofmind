import os
import sqlite3
import re
import time

conn = sqlite3.connect('pysom.db')
conn.create_function('REGEXP', 2, lambda x, y: 1 if re.search(x,y) else 0)
cursor = conn.cursor()

csv = open('out.csv', 'x')
csv.write('DayID;Relative;Absolute;Timestamp;Note\n')

cursor.execute(
	'''SELECT MAX(DayID) FROM "main.Mind";'''
)
db_len = cursor.fetchone()[0]

value = 0
for i in range(1, db_len+1):
    cursor.execute(
        '''SELECT * FROM "main.Mind"
        WHERE DayID = ?;''', (i,)
    )
    row = cursor.fetchone()
    value += row[1]
    csv.write('{};{};{};{};{}\n'.format(row[0], row[1], str(value), time.ctime(row[3]), row[2]))

csv.close()
