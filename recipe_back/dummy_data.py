import sqlite3 as db

conn = db.connect('./instance/flaskr.sqlite')
cursor = conn.cursor()
cursor.execute('insert into recipe values("01", "Bolognese", "Pasta, tomato, beef", "Lorem ipsum", "", "14/10/2025")')
cursor.execute('insert into recipe values("02", "Carbonara", "Pasta, egg, bacon", "Lorem ipsum", "", "12/10/2025")')
conn.commit()
conn.close()