import sqlite3
import json
from datetime import datetime
from .processing import processing

def set_completed():
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM tasks WHERE is_completed = 0""") #Print pending tasks to show user which ones can be marked as completed
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
    # Confirm updated entry in database with date_completed successfully changed
    cursor.execute("""SELECT * FROM tasks
                   WHERE id = ? AND date_completed IS NOT NULL""", (update_id))
    just_updated = cursor.fetchone()
    conn.close()
    processing()
    if just_updated: 
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

