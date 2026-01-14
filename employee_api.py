from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# 1️⃣ Connect to MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # <- replace with your MySQL password
        database="employee_db"
    )
    return conn

# 2️⃣ Add new employee performance
@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.json
    name = data.get('name')
    department = data.get('department')
    rating = data.get('rating')

    if not (name and department and rating):
        return jsonify({'error': 'Missing data'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO performance (name, department, rating) VALUES (%s, %s, %s)",
        (name, department, rating)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Employee added successfully'}), 201

# 3️⃣ Get all employee performances
@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM performance")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(employees), 200

# 4️⃣ Get employee by ID
@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM performance WHERE id = %s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()

    if employee:
        return jsonify(employee), 200
    else:
        return jsonify({'error': 'Employee not found'}), 404

# 5️⃣ Update employee performance
@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    name = data.get('name')
    department = data.get('department')
    rating = data.get('rating')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE performance SET name=%s, department=%s, rating=%s WHERE id=%s",
        (name, department, rating, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Employee updated successfully'}), 200

# 6️⃣ Delete employee
@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM performance WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Employee deleted successfully'}), 200

# 7️⃣ Get average rating per department
@app.route('/performance/summary', methods=['GET'])
def performance_summary():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT department, AVG(rating) AS average_rating, COUNT(*) AS employee_count
        FROM performance
        GROUP BY department
    """)
    summary = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(summary), 200

# 8️⃣ Get top performer per department
@app.route('/performance/top', methods=['GET'])
def top_performer():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT p1.department, p1.name, p1.rating
        FROM performance p1
        INNER JOIN (
            SELECT department, MAX(rating) AS max_rating
            FROM performance
            GROUP BY department
        ) p2
        ON p1.department = p2.department AND p1.rating = p2.max_rating
    """)
    top_employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(top_employees), 200

# 9️⃣ Run the app
if __name__ == '__main__':
    app.run(debug=True)
