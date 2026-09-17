from flask import Flask, redirect, url_for, render_template, request
import mysql.connector, os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

db_connection = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD")
}

def init_db():
    mysql_connection = mysql.connector.connect(**db_connection)
    return mysql_connection

conn = init_db()
c = conn.cursor(named_tuple=True)
c.execute("CREATE DATABASE IF NOT EXISTS employee_db")
c.execute("USE employee_db")
c.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(100), last_name VARCHAR(100), pay DECIMAL(10, 2), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

@app.route("/")
def index():
    c.execute("SELECT * FROM employee_db.employees")
    employees = c.fetchall()
    return render_template("index.html", employees=employees)

@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        pay = request.form["pay"]
        c.execute("INSERT INTO employee_db.employees (first_name, last_name, pay) VALUES (%s, %s, %s)", (first_name, last_name, pay))
        conn.commit()
        return redirect(url_for("index"))
    else:
        return render_template("add.html")

@app.route("/edit/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        pay = request.form["pay"]
        c.execute("UPDATE employee_db.employees SET first_name=%s, last_name=%s, pay=%s WHERE id=%s", (first_name, last_name, pay, employee_id))
        conn.commit()
        return redirect(url_for("index"))
    else:
        c.execute("SELECT * FROM employee_db.employees WHERE id=%s", (employee_id,))
        employee = c.fetchone()
        return render_template("edit.html", employee=employee)

@app.route("/delete/<int:employee_id>", methods=["POST"])
def delete_emp(employee_id):
    c.execute("DELETE FROM employee_db.employees WHERE id=%s", (employee_id,))
    conn.commit()
    return redirect(url_for("index"))

@app.route("/api/employees", methods=["GET", "POST", "PUT", "DELETE"])
def crud_employees():
    if request.method == "GET":
        c.execute("SELECT * FROM employee_db.employees")
        employees = c.fetchall()
        return {"employees": [dict(employee._asdict()) for employee in employees]}
    elif request.method == "POST":
        data = request.get_json()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        pay = data.get("pay")
        c.execute("INSERT INTO employee_db.employees (first_name, last_name, pay) VALUES (%s, %s, %s)", (first_name, last_name, pay))
        conn.commit()
        return {"message": "Employee added successfully"}, 201
    elif request.method == "PUT":
        data = request.get_json()
        employee_id = data.get("id")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        pay = data.get("pay")
        c.execute("UPDATE employee_db.employees SET first_name=%s, last_name=%s, pay=%s WHERE id=%s", (first_name, last_name, pay, employee_id))
        conn.commit()
        return {"message": "Employee updated successfully"}, 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)