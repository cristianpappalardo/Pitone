import sqlite3

conn = sqlite3.connect('library.sqlite3')
cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS books')
cur.execute('''CREATE TABLE books (
    isbn INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    copies INTEGER NOT NULL
)''')

cur.execute('DROP TABLE IF EXISTS users')
cur.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)''')

cur.execute('DROP TABLE IF EXISTS loans')
cur.execute('''CREATE TABLE loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    isbn INTEGER NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (isbn) REFERENCES books(isbn)
)''')

conn.commit()
conn.close()