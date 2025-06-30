from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Home Page – View all students
@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT, age INTEGER, department TEXT)''')
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('home.html', students=students)

# Add Student Page
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        dept = request.form['department']
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, department) VALUES (?, ?, ?)", (name, age, dept))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')

# Search Page
@app.route('/search', methods=['GET', 'POST'])
def search_student():
    results = []
    if request.method == 'POST':
        keyword = request.form['search']
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + keyword + '%',))
        results = cursor.fetchall()
        conn.close()
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
