import sqlite3

def get_db_connection():
    conn = sqlite3.connect('faces.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS faces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            features BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_face(name, features):
    features_bytes = features.tobytes()   
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO faces (name, features) VALUES (?, ?)', (name, features_bytes))
    conn.commit()
    conn.close()

def get_all_faces():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM faces')
    faces = c.fetchall()
    conn.close()
    return faces

def delete_face(id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM faces WHERE id = ?', (id,))
    conn.commit()
    conn.close()
