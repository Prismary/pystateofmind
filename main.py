import time
import os
import sqlite3
import re
import db_setup

if not os.path.isfile('pysom.db'):
    db_setup.setup()

conn = sqlite3.connect('pysom.db')
conn.create_function('REGEXP', 2, lambda x, y: 1 if re.search(x,y) else 0)
cursor = conn.cursor()

def get_stat(type):
    if type == 'day':
        cursor.execute(
			'''SELECT count(*) FROM "main.Mind";'''
        )
        return cursor.fetchone()[0]
    else:
        return '???'

# Program routine
print('''Welcome back to pyStateOfMind.
You are currently on day {} of your mental records.'''.format(str(get_stat('day')+1)))
print(
    '''
    ╔════════════╤═════════╤════════════╗
    ║  NEGATIVE  │ NEUTRAL │  POSITIVE  ║
    ╟────────────┼─────────┼────────────╢
    ║ -3  -2  -1 │    0    │  1   2   3 ║
    ╚════════════╧═════════╧════════════╝
    '''
)
print('''Please compare your mental condition to yesterday.
Choose one of the values from the scale above according to how your condition changed.'''
)
while True:
    dif = int(input('>> '))
    if dif >= -3 and dif <=3:
        break
    else:
        print('\n[!] Invalid value, please try again.')

note = input('\nThank you. Optionally, you may add a note for future reference.\n>> ')

cursor.execute(
    '''INSERT INTO "main.Mind" (Difference, Note, Timestamp)
    VALUES (?, ?, ?);''', (dif, note, int(time.time()))
)
conn.commit()

print('''\nYou have successfully completed day {} in your mental records. Thank you!
Good luck out there, see you tomorrow! ^-^/\n\n'''.format(str(get_stat('day'))))

print('(automatically exiting in 10 seconds...)')
time.sleep(10)
