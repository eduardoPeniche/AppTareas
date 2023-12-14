from .create import create_task
from .update import set_completed
from .read import read_tasks
from .delete import delete_task

def ask_user():
    while True: #Loop to keep asking until user enters 5 to exit app
        print()
        print("Menú Principal:")
        print(" (1) Crear tarea")
        print(" (2) Consultar tareas")
        print(" (3) Finalizar tarea")
        print(" (4) Eliminar tarea")
        print(" (5) Salir de la App")
        print()
        crud_answer = int(input("¿Qué operación deseas realizar? (1-5): "))

        if crud_answer in [1, 2, 3, 4, 5]: # this can be replaced with match-case in python version 3.10 ( Hever usa 3.9.6 )
            if crud_answer == 1:
                print()
                print("Ejecutar: Crear tarea")
                create_task()
            elif crud_answer == 2:
                print()
                print("Ejecutar: Consultar tarea")
                read_tasks()
            elif crud_answer == 3:
                print()
                print("Ejecutar: Actualizar tarea")
                set_completed()
            elif crud_answer == 4:
                print()
                print("Ejecutar: Eliminar tarea")
                delete_task()
            elif crud_answer == 5:
                print()
                print("Cerrando la App...")
                break #Exit loop and continue to main app
        else:
            print("¡ERROR!: Entrada invalida, debe ser un numero entre 1 y 5")