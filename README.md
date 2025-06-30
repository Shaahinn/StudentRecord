# 📘 Student Record Web App

A simple **Flask-based CRUD web application** for managing student records.  
This project allows users to add, view, and search student data using a browser interface and an SQLite database.

---

## 🚀 Features

- ✅ Add new student records
- 📋 View a list of all students
- 🔍 Search for students by name
- 💾 Data stored in SQLite database
- 🧩 Templating with HTML (Jinja2)
- 🖥️ Lightweight and beginner-friendly

---

## 🛠️ Technologies Used

| Component        | Technology          |
|------------------|---------------------|
| Backend          | Python, Flask       |
| Frontend         | HTML (Jinja2 templates) |
| Database         | SQLite              |
| Version Control  | Git + GitHub        |

---

## 📁 Project Structure

StudentRecordWeb/
├── app.py # Flask application
├── students.db # SQLite database (auto-generated)
└── templates/
├── home.html # View all students
├── add.html # Add new student
└── search.html # Search students by name

---

## 💡 How to Run the App Locally

1. **Clone the repo**  
```bash
git clone https://github.com/Shaahinn/StudentRecord.git
cd StudentRecord
pip install flask
python app.py
Visit: http://127.0.0.1:5000
