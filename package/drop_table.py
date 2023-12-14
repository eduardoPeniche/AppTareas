import sqlite3
# Module to delete the table and start over again. Must be run as main. Not accesible for user in main app.py
def drop_table():
    conn = sqlite3.connect("./taskapp.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS tasks""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_table()