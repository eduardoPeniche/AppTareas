import sqlite3
from datetime import datetime
import json


# Function to create table 'tasks' in taskapp.sqlite3
def create_table():
    # Create connection with database
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                is_completed INTEGER DEFAULT 0,
                date_created INTEGER NOT NULL,
                date_completed INTEGER)""")
    conn.commit()
    conn.close()

def create_task():
    name = input("Ingresa el nombre de la tarea: ")
    desc = input("Ingresa la descripción de la tarea: ")
    date_created = datetime.now()

    # Create connection with database
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO tasks (name, description, date_created)
                    VALUES (?, ?, ?)""", (name, desc, date_created))
    conn.commit()

    cursor.execute("""SELECT * FROM tasks
                   WHERE name = ? AND description = ? AND date_created = ?""", (name, desc, date_created))
    just_created = cursor.fetchall()
    conn.close()

    json_just_created = []
    for entry in just_created:
        entry_item = {
            "name": entry[1],
            "description": entry[2],
            "date_created": entry[4]
        }
        json_just_created.append(entry_item)

    return json.dumps(json_just_created, indent=4)
    