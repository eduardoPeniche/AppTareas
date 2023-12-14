from .create import create_task

def ask_user():
    print()
    print("Menú de Operaciones:")
    print(" (1) Crear tarea")
    print(" (2) Consultar tarea")
    print(" (3) Actualizar tarea")
    print(" (4) Eliminar tarea")
    print(" (5) Salir del programa")

    while True:
        print()
        crud_answer = int(input("¿Qué operación deseas realizar? (1-5): "))

        if crud_answer in [1, 2, 3, 4, 5]:
            if crud_answer == 1:
                print()
                print("Ejecutar: Crear tarea")
                print(create_task())
            elif crud_answer == 2:
                print()
                print("Ejecutar: Consultar tarea")
            elif crud_answer == 3:
                print()
                print("Ejecutar: Actualizar tarea")
            elif crud_answer == 4:
                print()
                print("Ejecutar: Eliminar tarea")
            elif crud_answer == 5:
                print()
                print("Finalizando Programa...")
        else:
            print("¡ERROR!: Entrada invalida, debe ser un numero entre 1 y 5")