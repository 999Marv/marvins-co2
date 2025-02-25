from db import get_db

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS co2_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ppm INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()

def add_reading(ppm: int, timestamp: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO co2_readings (ppm, timestamp) VALUES (?, ?)", (ppm, timestamp))
    conn.commit()

def get_all_readings():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT ppm, timestamp FROM co2_readings")
    return cursor.fetchall()
