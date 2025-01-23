import sqlite3
from datetime import datetime

DATABASE = 'patients.db'

class Patient:
    def __init__(self, full_name, age, sex, date_registered=None, image=""):
        self.full_name = full_name
        self.age = age
        self.sex = sex
        self.date_registered = date_registered or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.image = image

class PatientManager:
    @staticmethod
    def init_db():
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    sex TEXT NOT NULL,
                    date_registered TEXT NOT NULL,
                    image TEXT
                )
            ''')
            conn.commit()

    @staticmethod
    def add_patient(patient):
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO patients (full_name, age, sex, date_registered, image)
                VALUES (?, ?, ?, ?, ?)
            ''', (patient.full_name, patient.age, patient.sex, patient.date_registered, patient.image))
            patient_id = cursor.lastrowid
            conn.commit()
            return PatientManager.get_patient(patient_id)

    @staticmethod
    def get_patient(patient_id):
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "full_name": row[1],
                    "age": row[2],
                    "sex": row[3],
                    "date_registered": row[4],
                    "image": row[5]
                }
            return None

    @staticmethod
    def get_all_patients():
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM patients')
            rows = cursor.fetchall()
            return [
                {
                    "id": row[0],
                    "full_name": row[1],
                    "age": row[2],
                    "sex": row[3],
                    "date_registered": row[4],
                    "image": row[5]
                } for row in rows
            ]

    @staticmethod
    def update_patient(patient_id, updates):
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            fields = []
            values = []
            for key, value in updates.items():
                fields.append(f"{key} = ?")
                values.append(value)
            values.append(patient_id)
            query = f"UPDATE patients SET {', '.join(fields)} WHERE id = ?"
            cursor.execute(query, values)
            conn.commit()
            return PatientManager.get_patient(patient_id)