import sqlite3
from .processing import processing

def delete_task():
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()

    delete_id = input(" ---> Qué tarea deseas eliminar? Ingresa el id: ")

    cursor.execute("""DELETE FROM tasks
                   WHERE id = ?""", (delete_id))
    conn.commit()
    # Confirm the entry was successfully deleted
    cursor.execute("""SELECT * FROM tasks
                   WHERE id = ?""", (delete_id))
    just_deleted = cursor.fetchone()
    conn.close()
    processing()
    print()
    if just_deleted:
        print("Lo siento, algo falló, tarea no eliminada")
    else:
        print("Operación Exitosa: Tarea ELIMINADA")