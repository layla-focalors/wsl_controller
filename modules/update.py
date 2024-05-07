import sqlite3

def connect_database():
    con1 = sqlite3.connect('settings.db')
    cursor = con1.cursor()
    
    con1.commit()
    
    return cursor

def save_database(con):
    return True

def create_version_table():
    cursor = connect_database()
    cursor.execute("CREATE TABLE IF NOT EXISTS settings (version TEXT);")
    if save_database(cursor) == False:
        print("Error 101 saving database")
    return True

def update_version(version):
    cursor = connect_database()
    insert_sql = f"INSERT INTO settings (version) VALUES ('{version}');"
    cursor.execute(insert_sql)
    if save_database(cursor) == False:
        print("Error 102 saving database")
    return True
    
def get_version():
    cursor = connect_database()
    cursor.execute("SELECT * FROM settings;")
    version = cursor.fetchone()
    return version[0]
