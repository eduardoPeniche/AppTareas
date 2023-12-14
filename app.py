import sqlite3
import json
import datetime
from package.create import create_table
from package.interactive import ask_user
# import (cambiar color de menu en terminal)

# main app
# modulos: tablas, inserción, menu

def main():
    print("-- APP PARA REGISTRO DE TAREAS --")
    create_table()

    ask_user()

if __name__ == "__main__":
    main()