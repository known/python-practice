import sqlite3
from flask import g, current_app


def connect_db():
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db
