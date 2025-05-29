# 🏥 Hospital Management System

A simple and modular web-based **Hospital Management System** built with **Flask** and **SQLite**. The application currently supports basic operations like managing patients, doctors, and appointments with a clean dark theme UI and animated design.

---

## 🚀 Features (Current)

- 🔹 Add, view, and manage **patients**
- 🔹 Add, view, and manage **doctors**
- 🔹 Schedule and delete **appointments**
- 🔹 Modern dark-themed UI with **gradient background**
- 🔹 **Responsive layout** using HTML and CSS
- 🔹 Animated transitions and hover effects

---

## 🛠️ Tech Stack

| Layer       | Technology     |
|-------------|----------------|
| Backend     | Python, Flask  |
| Database    | SQLite         |
| Frontend    | HTML, CSS      |
| Styling     | Custom CSS with gradient & animation |

---

## 📁 Project Structure
```
hospital-management/
├── app.py # Main Flask application
├── static/
│ └── styles.css # Gradient dark theme & animations
├── templates/
│ ├── base.html # Layout base with navigation
│ ├── index.html # Homepage
│ ├── patients.html # Display all patients
│ ├── add_patient.html # Add a new patient
│ ├── doctors.html # Display all doctors
│ ├── add_doctor.html # Add a new doctor
│ ├── appointments.html # Display all appointments
```

---

## 💾 Database Schema

The database file `hospital.db` is auto-generated when the project runs for the first time.

**Tables:**
- `patients`: `id`, `name`, `age`, `gender`, `contact`
- `doctors`: `id`, `name`, `specialization`, `contact`
- `appointments`: `id`, `patient_id`, `doctor_id`, `date`, `time`

---

## 🧪 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/hospital-management.git
   cd hospital-management

---

## 💾 Database Schema

The database file `hospital.db` is auto-generated when the project runs for the first time.

**Tables:**
- `patients`: `id`, `name`, `age`, `gender`, `contact`
- `doctors`: `id`, `name`, `specialization`, `contact`
- `appointments`: `id`, `patient_id`, `doctor_id`, `date`, `time`

---

## 🧪 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/hospital-management.git
   cd hospital-management
```
│ └── add_appointment.html # Add a new appointment
├── hospital.db # SQLite database file (auto-generated)
└── README.md # Project overview and documentationnt
└── README.md # Project documentation
```
2.Install Flask
```bash
pip install flask
```
3. Run the Flask app
```bash
python app.py
```
4.Open in browser:
http://127.0.0.1:5000

---

### 📌 Current Limitations
- No user authentication (admin, doctor, or patient login)

- No validation or input sanitization

- Basic database operations only (CRUD)

- No search or filter functionality
 ---

### 🚀 Future Enhancements (Planned)
✅ Add authentication (login/signup for staff and admins)

✅ Add search & filtering for records

✅ Export reports (PDF, Excel)

✅ Dashboard analytics for appointments and doctors

✅ Add image upload and patient medical records

✅ Implement responsive design with Bootstrap or Tailwind CSS

✅ Migrate database to MySQL/PostgreSQL for production

---

Feel free to fork, enhance, and contribute to this project.








