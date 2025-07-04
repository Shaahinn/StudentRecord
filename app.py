from flask import Flask, render_template, request, redirect
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# ---------------- Home Page Route ----------------
# This route displays all student records stored in the database
@app.route('/')
def home():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Create the students table if it doesn't already exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT, 
                      age INTEGER, 
                      department TEXT)''')

    # Fetch all student records
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Render the home page with student data
    return render_template('home.html', students=students)

# ---------------- Add Student Route ----------------
# This route handles adding a new student via form submission
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Get form data submitted by user
        name = request.form['name']
        age = request.form['age']
        dept = request.form['department']

        # Insert the new student data into the database
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, department) VALUES (?, ?, ?)", (name, age, dept))
        conn.commit()
        conn.close()

        # Redirect to home page after successful addition
        return redirect('/')
    
    # Render the form page if it's a GET request
    return render_template('add.html')

# ---------------- Search Student Route ----------------
# This route allows users to search for students by name
@app.route('/search', methods=['GET', 'POST'])
def search_student():
    results = []  # Initialize empty results list

    if request.method == 'POST':
        # Get the search keyword entered by user
        keyword = request.form['search']

        # Search the database for matching names
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + keyword + '%',))
        results = cursor.fetchall()
        conn.close()

    # Render the search results page
    return render_template('search.html', results=results)

# ---------------- Run the Flask App ----------------
if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
