import sqlite3
from faker import Faker
import random


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

fake = Faker()

cursor.executescript('''
    DROP TABLE IF EXISTS students;
    CREATE TABLE students (
        student_name TEXT
    );

    DROP TABLE IF EXISTS teachers;
    CREATE TABLE teachers (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_name TEXT
    );

    DROP TABLE IF EXISTS subjects;
    CREATE TABLE subjects (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT,
        teacher_name TEXT
    );

    DROP TABLE IF EXISTS grades;
    CREATE TABLE grades (
        student_name,
        subject_name,
        grade1 INTEGER,
        date_received1 TEXT,
        grade2 INTEGER,
        date_received2 TEXT,
        grade3 INTEGER,
        date_received3 TEXT,
        grade4 INTEGER,
        date_received4 TEXT,
        FOREIGN KEY (student_name) REFERENCES students(student_name),
        FOREIGN KEY (subject_name) REFERENCES subjects(subject_name)
    );
    
    DROP TABLE IF EXISTS groups;
    CREATE TABLE groups (
        group_name TEXT,
        student_name TEXT
    );
''')

def add_students(num_students):
    students = []
    for _ in range(num_students):
        student_name = fake.name()
        students.append((student_name,))

    cursor.executemany('''
        INSERT INTO students (student_name)
        VALUES (?)
    ''', students)
    conn.commit()



def add_teachers(num_teachers):
    teachers = []
    for _ in range(num_teachers):
        teacher_name = fake.name()
        teachers.append((teacher_name,))

    cursor.executemany('''
        INSERT INTO teachers (teacher_name)
        VALUES (?)
    ''', teachers)
    conn.commit()


def add_subjects():
    subjects = []
    teacher_names = [row[0] for row in cursor.execute('SELECT teacher_name FROM teachers').fetchall()]

    for teacher_name in teacher_names:
        subject_name = fake.word()
        subjects.append((subject_name, teacher_name))

    cursor.executemany('''
        INSERT INTO subjects (subject_name, teacher_name)
        VALUES (?, ?)
    ''', subjects)
    conn.commit()

def add_grades():
    student_names = [row[0] for row in cursor.execute('SELECT student_name FROM students').fetchall()]
    subject_names = [row[0] for row in cursor.execute('SELECT subject_name FROM subjects').fetchall()]

    for student_name in student_names:
        for subject_name in subject_names:
            grade1 = fake.random_int(1, 100)
            date_received1 = fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")
            grade2 = fake.random_int(1, 100)
            date_received2 = fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")
            grade3 = fake.random_int(1, 100)
            date_received3 = fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")
            grade4 = fake.random_int(1, 100)
            date_received4 = fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d")
            cursor.execute('''
                       INSERT INTO grades (student_name, subject_name, grade1, date_received1, 
                       grade2,date_received2, grade3, date_received3, grade4, date_received4)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ''', (student_name, subject_name, grade1, date_received1,
                       grade2,date_received2, grade3, date_received3, grade4, date_received4))
    conn.commit()

def add_groups():
    students = [row[0] for row in cursor.execute('SELECT student_name FROM students').fetchall()]

    for student_name in students:
        group_name = random.choice(['A', 'B', 'C'])
        cursor.execute('''
            INSERT INTO groups (group_name, student_name)
            VALUES (?, ?)
        ''', (group_name, student_name))
    conn.commit()

add_students(30)
add_teachers(5)
add_subjects()
add_grades()
add_groups()
conn.close()
