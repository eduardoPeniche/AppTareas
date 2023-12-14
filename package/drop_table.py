import sqlite3

def drop_table():
    conn = sqlite3.connect("./taskapp.sqlite3")
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS tasks""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    drop_table()