from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'hospital.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create patients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            contact TEXT
        )
    ''')

    # Create doctors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT,
            contact TEXT
        )
    ''')

    # Create appointments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY(patient_id) REFERENCES patients(id),
            FOREIGN KEY(doctor_id) REFERENCES doctors(id)
        )
    ''')

    conn.commit()
    conn.close()

# Always ensure tables exist
init_db()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()
    return render_template('patients.html', patients=patients)

@app.route('/patients/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        contact = request.form.get('contact')

        conn = get_db_connection()
        conn.execute('INSERT INTO patients (name, age, gender, contact) VALUES (?, ?, ?, ?)',
                     (name, age, gender, contact))
        conn.commit()
        conn.close()
        return redirect(url_for('patients'))
    return render_template('add_patient.html')

@app.route('/doctors')
def doctors():
    conn = get_db_connection()
    doctors = conn.execute('SELECT * FROM doctors').fetchall()
    conn.close()
    return render_template('doctors.html', doctors=doctors)

@app.route('/doctors/add', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        name = request.form.get('name')
        specialization = request.form.get('specialization')
        contact = request.form.get('contact')

        conn = get_db_connection()
        conn.execute('INSERT INTO doctors (name, specialization, contact) VALUES (?, ?, ?)',
                     (name, specialization, contact))
        conn.commit()
        conn.close()
        return redirect(url_for('doctors'))
    return render_template('add_doctor.html')

@app.route('/doctors/edit/<int:doctor_id>', methods=['GET', 'POST'])
def edit_doctor(doctor_id):
    conn = get_db_connection()
    doctor = conn.execute('SELECT * FROM doctors WHERE id = ?', (doctor_id,)).fetchone()
    conn.close()

    if request.method == 'POST':
        name = request.form.get('name')
        specialization = request.form.get('specialization')
        contact = request.form.get('contact')

        conn = get_db_connection()
        conn.execute('UPDATE doctors SET name = ?, specialization = ?, contact = ? WHERE id = ?',
                     (name, specialization, contact, doctor_id))
        conn.commit()
        conn.close()
        return redirect(url_for('doctors'))

    return render_template('edit_doctor.html', doctor=doctor)

@app.route('/appointments')
def appointments():
    conn = get_db_connection()
    appointments = conn.execute('''
        SELECT appointments.id, patients.name AS patient_name,
               doctors.name AS doctor_name, appointments.date, appointments.time
        FROM appointments
        JOIN patients ON appointments.patient_id = patients.id
        JOIN doctors ON appointments.doctor_id = doctors.id
    ''').fetchall()
    conn.close()
    return render_template('appointments.html', appointments=appointments)

@app.route('/appointments/add', methods=['GET', 'POST'])
def add_appointment():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    doctors = conn.execute('SELECT * FROM doctors').fetchall()
    conn.close()

    if request.method == 'POST':
        patient_id = request.form.get('patient_id')
        doctor_id = request.form.get('doctor_id')
        date = request.form.get('date')
        time = request.form.get('time')

        conn = get_db_connection()
        conn.execute('INSERT INTO appointments (patient_id, doctor_id, date, time) VALUES (?, ?, ?, ?)',
                     (patient_id, doctor_id, date, time))
        conn.commit()
        conn.close()
        return redirect(url_for('appointments'))

    return render_template('add_appointment.html', patients=patients, doctors=doctors)

@app.route('/appointments/delete/<int:appointment_id>', methods=['GET'])
def delete_appointment(appointment_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('appointments'))

@app.route('/doctors/delete/<int:doctor_id>', methods=['GET'])
def delete_doctor(doctor_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM doctors WHERE id = ?', (doctor_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('doctors'))

# Debug routes (optional)
@app.route('/debug/schema')
def debug_schema():
    conn = get_db_connection()
    schema = conn.execute("PRAGMA table_info(appointments)").fetchall()
    conn.close()
    return {'schema': [dict(row) for row in schema]}

@app.route('/debug/appointments')
def debug_appointments():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM appointments").fetchall()
    conn.close()
    return {'appointments': [dict(row) for row in data]}

@app.route('/debug/db_exists')
def debug_db_exists():
    return {'db_exists': os.path.exists(DATABASE)}


if __name__ == '__main__':
    app.run(debug=True)
