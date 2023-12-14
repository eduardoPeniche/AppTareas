import sqlite3
import json
from .processing import processing

def read_tasks():
    while True:
        print()
        print("Elige una opción de Consulta:")
        print(" (1) Mostrar todas las tareas")
        print(" (2) Mostrar tareas pendientes")
        print(" (3) Mostrar tareas completadas")
        print(" (4) Mostrar tarea con ID especifico")
        print(" (5) Regresar al Menú Principal")
        print()
        read_answer = int(input("¿Qué tareas deseas consultar? (1-5): "))

        if read_answer in [1, 2, 3, 4, 5]:
            if read_answer == 1:
                print()
                print("Ejecutar: Mostrar todas las tareas")
                show_all_tasks()
            elif read_answer == 2:
                print()
                print("Ejecutar: Mostrar tareas pendientes")
                show_pending_tasks()
            elif read_answer == 3:
                print()
                print("Ejecutar: Mostrar tareas completadas")
                show_complete_tasks()
            elif read_answer == 4:
                print()
                print("Ejecutar: Mostrar tarea con ID especifico")
                show_id_task()
            elif read_answer == 5:
                print()
                print("Regresando al Menú Principal")
                processing()
                print()
                break
        else:
            print("¡ERROR!: Entrada invalida, debe ser un numero entre 1 y 5")

def show_all_tasks():
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM tasks""")
    all_tasks = cursor.fetchall()
    conn.close()

    json_all_tasks = []
    for task in all_tasks:
        task_entry = {
            "id": task[0],
            "name": task[1],
            "description": task[2],
            "date_created": task[4],
            "date_completed": task[5]
        }
        json_all_tasks.append(task_entry)
    print("Tareas:")
    processing()
    print()
    print(json.dumps(json_all_tasks, indent=4))

def show_pending_tasks():
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM tasks WHERE is_completed = 0""")
    not_completed = cursor.fetchall()
    conn.close()

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
    processing()
    print()
    print(json.dumps(json_not_completed, indent=4))

def show_complete_tasks():
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM tasks WHERE is_completed = 1""")
    completed = cursor.fetchall()
    conn.close()

    json_completed = []
    for task in completed:
        task_entry = {
            "id": task[0],
            "name": task[1],
            "description": task[2],
            "date_created": task[4]
        }
        json_completed.append(task_entry)
    print("Tareas Finalizadas:")
    processing()
    print()
    print(json.dumps(json_completed, indent=4))

def show_id_task():
    conn = sqlite3.connect("taskapp.sqlite3")
    cursor = conn.cursor()

    read_id = input(" ---> Qué tarea deseas consultar? Ingresa el id: ")

    cursor.execute("""SELECT * FROM tasks
                   WHERE id = ?""", (read_id))
    id_selected = cursor.fetchone()
    conn.close()

    if id_selected: #Verify a row was found
        processing() 
        print()
        print("Tarea ENCONTRADA:")
        json_id_selected = {
            "name": id_selected[1],
            "description": id_selected[2],
            "is_completed": id_selected[3],
            "date_created": id_selected[4],
            "date_completed": id_selected[5]
        }

    print(json.dumps(json_id_selected, indent=4))