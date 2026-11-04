   
import os
import sqlite3

def create_database():
    db_path = os.path.join(os.path.dirname(__file__), "db_name.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # AUTOINCREMENT hata diya
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            cid INTEGER PRIMARY KEY,
            courseNAME TEXT UNIQUE,
            Duration TEXT,
            Charges TEXT,
            Description TEXT
        )
    """)
    conn.commit()
    conn.close()


def insert_course(courseNAME, Duration, Charges, Description):
    db_path = os.path.join(os.path.dirname(__file__), "db_name.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Pehle missing ID (gap) dhoondho
    cur.execute("SELECT cid FROM course ORDER BY cid")
    ids = [row[0] for row in cur.fetchall()]

    # Agla available ID nikalna (chhoti se chhoti missing number)
    new_id = 1
    for i in ids:
        if i == new_id:
            new_id += 1
        else:
            break

    # Record insert karo manually ID ke sath
    cur.execute("""
        INSERT INTO course (cid, courseNAME, Duration, Charges, Description)
        VALUES (?, ?, ?, ?, ?)
    """, (new_id, courseNAME, Duration, Charges, Description))

    conn.commit()
    conn.close()

    print(f"✅ Course added with ID: {new_id}")
