import sqlite3

conn = sqlite3.connect('books.db')
conn.execute('CREATE TABLE books (isbn INTEGER PRIMARY KEY AUTOINCREMENT, image TEXT, author TEXT, title TEXT, price FLOAT)')
conn.close()

