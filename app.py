"""Flask application for managing employee and role records in a MySQL database."""

import os
from flask import Flask, redirect, url_for, render_template, request
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

db_connection = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD")
}

def init_db():
    try:
        mysql_connection = mysql.connector.connect(**db_connection)
        return mysql_connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

conn = init_db()
c = conn.cursor(named_tuple=True)
c.execute("CREATE DATABASE IF NOT EXISTS employee_db")
c.execute("USE employee_db")
c.execute("CREATE TABLE IF NOT EXISTS roles (id INT AUTO_INCREMENT PRIMARY KEY, role_name VARCHAR(100), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
c.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(100), last_name VARCHAR(100), pay DECIMAL(10, 2), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, roles_id INT, FOREIGN KEY (roles_id) REFERENCES roles(id))")

employee_pages=[
    'index',
    'add_employee',
    'edit_employee'
]

role_pages=[
    'roles',
    'add_role',
    'edit_role'
]

@app.route("/")
def index():
    c.execute("""SELECT e.id, e.first_name, e.last_name, e.pay, e.created_at, e.roles_id, r.role_name 
                 FROM employees e 
                 LEFT JOIN roles r ON e.roles_id = r.id""")
    employees = c.fetchall()
    return render_template("index.html", employees=employees, employee_pages=employee_pages, role_pages=role_pages)

@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        pay = request.form["pay"]
        roles_id = request.form["roles_id"]
        c.execute("INSERT INTO employee_db.employees (first_name, last_name, pay, roles_id) VALUES (%s, %s, %s, %s)", (first_name, last_name, pay, roles_id))
        conn.commit()
        return redirect(url_for("index"))
    else:
        c.execute("SELECT * FROM employee_db.roles")
        roles_list = c.fetchall()
        return render_template("add.html", roles_list=roles_list, employee_pages=employee_pages, role_pages=role_pages)

@app.route("/edit/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        pay = request.form["pay"]
        roles_id = request.form["roles_id"]
        c.execute("UPDATE employee_db.employees SET first_name=%s, last_name=%s, pay=%s ,roles_id=%s WHERE id=%s", (first_name, last_name, pay, roles_id, employee_id))
        conn.commit()
        return redirect(url_for("index"))
    else:
        c.execute("SELECT * FROM employee_db.employees WHERE id=%s", (employee_id,))
        employee = c.fetchone()
        c.execute("SELECT * FROM employee_db.roles")
        roles_list = c.fetchall()
        return render_template("edit.html", employee=employee, roles_list=roles_list, employee_pages=employee_pages, role_pages=role_pages)

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
    elif request.method == "DELETE":
        data = request.get_json()
        employee_id = data.get("id")
        c.execute("DELETE FROM employee_db.employees WHERE id=%s", (employee_id,))
        conn.commit()
        return {"message": "Employee deleted successfully"}, 200

@app.route("/roles", methods=["GET", "POST"])
def roles():
    c.execute("SELECT * FROM employee_db.roles")
    roles_list = c.fetchall()
    return render_template("roles.html", roles_list=roles_list, employee_pages=employee_pages, role_pages=role_pages)

@app.route("/add-role", methods=["GET", "POST"])
def add_role():
    if request.method == "POST":
        role_name = request.form["role_name"]
        c.execute("INSERT INTO employee_db.roles (role_name) VALUES (%s)", (role_name,))
        conn.commit()
        return redirect(url_for("roles"))
    else:
        return render_template("add_role.html", employee_pages=employee_pages, role_pages=role_pages)

@app.route("/edit-roles/<int:role_id>", methods=["GET", "POST"])
def edit_role(role_id):
    if request.method == "POST":
        role_name = request.form["role_name"]
        c.execute("UPDATE employee_db.roles SET role_name=%s WHERE id=%s", (role_name, role_id,))
        conn.commit()
        return redirect(url_for("roles"))
    else:
        c.execute("SELECT * FROM employee_db.roles WHERE id=%s", (role_id,))
        roles_list = c.fetchone()
        return render_template("edit_role.html", roles_list=roles_list, employee_pages=employee_pages, role_pages=role_pages)

@app.route("/delete-role/<int:role_id>", methods=["POST"])
def delete_role(role_id):
    c.execute("DELETE FROM employee_db.roles WHERE id=%s", (role_id,))
    conn.commit()
    return redirect(url_for("roles"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)