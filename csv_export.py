import os
import sqlite3
import re

conn = sqlite3.connect('pysom.db')
conn.create_function('REGEXP', 2, lambda x, y: 1 if re.search(x,y) else 0)
cursor = conn.cursor()

csv = open('out.csv', 'x')

cursor.execute(
	'''SELECT MAX(DayID) FROM "main.Mind";'''
)
db_len = cursor.fetchone()[0]

value = 0
for i in range(1, db_len+1):
    cursor.execute(
        '''SELECT Difference FROM "main.Mind"
        WHERE DayID = ?;''', (i,)
    )
    value += cursor.fetchone()[0]
    csv.write(str(value)+'\n')

csv.close()
