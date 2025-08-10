import sqlite3

DB_NAME = "images.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS images (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        filename TEXT,
                        label TEXT
                    )''')
    conn.commit()
    conn.close()

def add_image(filename, label):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (filename, label) VALUES (?, ?)", (filename, label))
    conn.commit()
    conn.close()

def get_all_images():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM images")
    data = cursor.fetchall()
    conn.close()
    return data

def get_image(image_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM images WHERE id=?", (image_id,))
    data = cursor.fetchone()
    conn.close()
    return data

def update_image(image_id, label):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE images SET label=? WHERE id=?", (label, image_id))
    conn.commit()
    conn.close()

def delete_image(image_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM images WHERE id=?", (image_id,))
    conn.commit()
    conn.close()
