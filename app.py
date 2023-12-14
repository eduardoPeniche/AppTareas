from package.create import create_table
from package.interactive import ask_user
import sys

def main():
    print("-- APP PARA REGISTRO DE TAREAS --")

    create_table() #Create sqlite3 db 
    ask_user() #Interactive CRUD menu
    
    print()
    print("App Finalizada")
    sys.exit()

if __name__ == "__main__":
    main()