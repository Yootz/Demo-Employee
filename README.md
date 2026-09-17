# Employee Management System

A web-based employee data management system using Python Flask, MySQL, and CRUD operations.

## Features

- ✅ Create new employee records (First Name, Last Name, Pay)
- ✅ Read/View all employee records
- ✅ Update existing employee information
- ✅ Delete employee records
- ✅ Responsive web interface
- ✅ MySQL database integration
- ✅ RESTful API endpoints

## Prerequisites

- Python 3.7 or higher
- MySQL Server installed and running
- pip (Python package manager)

## Installation & Setup

### 1. Install Python Dependencies

```bash
cd "CRUD Database"
pip install -r requirements.txt
```

### 2. Create MySQL Database

Before running the application, create a MySQL database:

```sql
CREATE DATABASE employee_db;
```

### 3. Configure Database Connection

Edit `.env` and update the database configuration:

```python
DB_HOST='localhost'
DB_USER='root'
DB_PASSWORD='your_password'
```

### 4. Run the Application

```bash
python app.py
```

The application will:
- Initialize the database and create the employees table
- Start the Flask development server
- Be accessible at `http://localhost:5000`

## Usage

### Web Interface

1. **View Employees** - Navigate to the home page to see all employees
2. **Add Employee** - Click "Add Employee" to add a new employee record
   - Fill in First Name, Last Name, and Pay
   - Click "Add Employee" to save
3. **Edit Employee** - Click the "Edit" button on any employee row
   - Modify the information and click "Update Employee"
4. **Delete Employee** - Click the "Delete" button and confirm
   - The employee record will be permanently deleted

### API Endpoints

```
GET    /api/employees              - Get all employees
POST   /api/employees              - Create a new employee
PUT    /api/employees/<id>         - Update an employee
DELETE /api/employees/<id>         - Delete an employee
```

#### Example API Usage

**Get all employees:**
```bash
curl http://localhost:5000/api/employees
```

**Create an employee:**
```bash
curl -X POST http://localhost:5000/api/employees \
  -H "Content-Type: application/json" \
  -d '{"first_name":"John","last_name":"Doe","pay":50000}'
```

**Update an employee:**
```bash
curl -X PUT http://localhost:5000/api/employees/1 \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Jane","last_name":"Doe","pay":55000}'
```

**Delete an employee:**
```bash
curl -X DELETE http://localhost:5000/api/employees/1
```

## Project Structure

```
CRUD Database/
├── app.py                 # Main Flask application with CRUD logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Employee list page
│   ├── add.html          # Add employee form
│   └── edit.html         # Edit employee form
└── static/
    └── css/
        └── style.css     # Stylesheet
```

## Database Schema

The system uses a single `employees` table:

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    pay DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## CRUD Operations

### Create
- Add new employee records through the web form or API
- Data validation for required fields
- Automatic timestamp on record creation

### Read
- View all employees in a sortable table
- Sort by most recent employees first
- View total employee count
- Access individual employee details via API

### Update
- Edit existing employee information
- Update any field (first name, last name, pay)
- Changes are immediately reflected in the database

### Delete
- Remove employee records with confirmation
- Soft/hard delete depending on requirement
- Cascade operations if needed

## Troubleshooting

### MySQL Connection Error
- Ensure MySQL server is running
- Check username and password in `app.py`
- Verify database exists: `CREATE DATABASE employee_db;`

### Table Not Created
- The table is created automatically when app.py runs
- If it fails, manually run the SQL in `app.py` (lines 27-37)

### Port Already in Use
- Change the port in app.py: `app.run(debug=True, port=5001)`
- Or kill the process using port 5000

## Development

### Enable Debug Mode
Debug mode is already enabled in app.py. The application will:
- Auto-reload on code changes
- Display detailed error messages
- Enable interactive debugger

### Testing
Run the test file for unit tests:
```bash
python test.py
```

## Security Notes

⚠️ **Important for Production:**
- Change database password in `app.py`
- Set `debug=False` in production
- Use environment variables for sensitive data
- Implement user authentication
- Add input validation and sanitization
- Use HTTPS for data transmission
- Implement rate limiting

## Features to Add

- User authentication & authorization
- Search and filter functionality
- Employee department/roles
- Salary history tracking
- Bulk import/export
- Export to PDF/Excel
- Department management
- Performance tracking

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please refer to the code comments or create an issue in your repository.

---

**Last Updated:** September 2026
