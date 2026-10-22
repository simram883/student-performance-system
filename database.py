import sqlite3
DB_NAME = "student_db.sqlite3"
def connect():
    return sqlite3.connect(DB_NAME)
def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (roll_no INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, gender TEXT, course TEXT, mobile TEXT, email TEXT, address TEXT)
    """)
    conn.commit()
    conn.close()
def insert_student(data):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(""" INSERT INTO students (roll_no, name, age, gender, course, mobile, email, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()
def update_student(old_roll_no, data):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET roll_no=?, name=?, age=?, gender=?, course=?,
            mobile=?, email=?, address=?
        WHERE roll_no=?
    """, (
        data[0], data[1], data[2], data[3],
        data[4], data[5], data[6], data[7],
        old_roll_no
    ))
    conn.commit()
    conn.close()
def delete_student(roll_no):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll_no,)
    )
    conn.commit()
    conn.close()
def get_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT roll_no, name, age, gender, course, mobile, email, address FROM students ORDER BY roll_no""")
    rows = cursor.fetchall()
    conn.close()
    return rows
def search_student(roll_no):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT roll_no, name, age, gender, course,  mobile, email, address FROM students WHERE roll_no=?""", (roll_no,))
    rows = cursor.fetchall()
    conn.close()
    return rows