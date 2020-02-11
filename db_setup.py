import sqlite3

def setup():
    with sqlite3.connect('pysom.db') as db:
        db.execute(
            '''CREATE TABLE IF NOT EXISTS "main.Mind"(
            DayID INTEGER PRIMARY KEY,
            Difference INTEGER,
            Note TEXT,
            Timestamp INTEGER
            );'''
        )

        db.commit()
    return 'Database setup complete.'
