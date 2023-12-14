import sqlite3
from datetime import datetime
import json
from .processing import processing


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
    date_created = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

    # Create connection with database
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO tasks (name, description, date_created)
                    VALUES (?, ?, ?)""", (name, desc, date_created))
    conn.commit()

    cursor.execute("""SELECT * FROM tasks
                   WHERE name = ? AND description = ? AND date_created = ?""", (name, desc, date_created))
    just_created = cursor.fetchone()
    conn.close()

    if just_created: #Verify a row was found
        processing() 
        print()
        print("Creación de tarea EXITOSA")
        print("Confirmación de entrada en Base de Datos:") 
        json_just_created = {
            "name": just_created[1],
            "description": just_created[2],
            "date_created": just_created[4]
        }

    return json.dumps(json_just_created, indent=4)