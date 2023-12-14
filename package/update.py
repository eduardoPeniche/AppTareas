import sqlite3
import json
from datetime import datetime
from .processing import processing

def set_completed():
    # Create connection with database
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM tasks WHERE is_completed = 0""")
    not_completed = cursor.fetchall()

    json_not_completed = []
    for task in not_completed:
        task_entry = {
            "id": task[0],
            "name": task[1],
            "description": task[2],
            "date_created": task[4]
        }
        json_not_completed.append(task_entry)
    print("Tareas Pendientes:")
    print(json.dumps(json_not_completed, indent=4))

    update_id = input(" ---> Qué tarea deseas marcar como completada? Ingresa el id: ")

    update_completed = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

    cursor.execute("""UPDATE tasks
                   SET is_completed = 1,
                   date_completed = ?
                   WHERE id = ?""", (update_completed, update_id))
    conn.commit()

    cursor.execute("""SELECT * FROM tasks
                   WHERE id = ? """, (update_id))
    just_updated = cursor.fetchone()
    conn.close()

    if just_updated: #Verify a row was found
        processing() 
        print()
        print("Actualización de tarea EXITOSA")
        print("Confirmación de entrada en Base de Datos:") 
        json_just_updated = {
            "name": just_updated[1],
            "description": just_updated[2],
            "date_created": just_updated[4],
            "date_completed": just_updated[5]
        }

    print(json.dumps(json_just_updated, indent=4))

