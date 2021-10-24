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

def complete(id):
    def _complete():
        print(id)
    return _complete


def render_todos():
    rows = crs.execute("SELECT * FROM todo").fetchall()
    #print(len(rows))
    #print(rows)
    
    for i in range(0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        cb = Checkbutton(frame, text=description, width=42, anchor="w", command=complete(id))
        cb.grid(row=i, column=0, sticky="w")


def add_todo():
    todo = todo_entry.get()
    if todo:
        crs.execute("""
                INSERT INTO todo (description, completed) VALUES (?, ?)
        """, (todo, False))
        connec.commit()
        todo_entry.delete(0, "end")
        render_todos()
    else:
        pass    


label_name = Label(window, text="Tarea")
label_name.grid(row=0, column=0)

todo_entry = Entry(window, width=40)
todo_entry.grid(row=0, column=1)

btn = Button(window, text="Agregar", command=add_todo)
btn.grid(row=0, column=2)

frame = LabelFrame(window, text="Mis tareas", padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky="nswe", padx=5)

todo_entry.focus()


window.bind('<Return>', lambda x: add_todo())

render_todos()
window.mainloop()