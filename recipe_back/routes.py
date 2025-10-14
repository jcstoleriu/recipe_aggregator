from index import app
import time
from flask import g

import sqlite3 as sql

@app.route('/api/time')
def get_time():
    return {'time': time.time()}


@app.route('/api/recipes')
def get_recipes():
    db = sql.connect('./instance/flaskr.sqlite')
    cursor = db.cursor()
    cursor.execute('select * from recipe')
    return cursor.fetchall()
