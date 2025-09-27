import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")
cursor.execute("INSERT OR IGNORE INTO users(username,password) VALUES (?,?)", ("admin","admin123"))

# Patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    sex TEXT,
    phone TEXT,
    address TEXT,
    disease TEXT,
    appointment TEXT,
    room_no TEXT,
    admission_date TEXT,
    discharge_date TEXT
)
""")

# Employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dept TEXT
)
""")

# Rooms table
cursor.execute("""
CREATE TABLE IF NOT EXISTS rooms(
    room_no TEXT PRIMARY KEY,
    type TEXT,
    status TEXT
)
""")

# Appointments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    doctor_name TEXT,
    date TEXT,
    time TEXT
)
""")

# Billing table
cursor.execute("""
CREATE TABLE IF NOT EXISTS billing(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    amount REAL,
    date TEXT
)
""")

conn.commit()
conn.close()



