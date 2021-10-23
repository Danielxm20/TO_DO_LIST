from sqlite3.dbapi2 import Cursor
from tkinter import *
import sqlite3

window = Tk()
window.title("TODO LIST")
window.geometry("500x500")

connec = sqlite3.connect("todo.db")

crs = connec.cursor()
crs.execute("""
    CREATE TABLE if not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN
    );

""")

connec.commit()

window.mainloop()