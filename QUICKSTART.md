# QUICK START GUIDE

## Step 1: Install Python Packages
```
pip install -r requirements.txt
```

## Step 2: Setup MySQL Database
Make sure MySQL is installed and running.

Option A - Run the setup script:
```
python setup_db.py
```

Option B - Manual setup in MySQL Console:
```sql
CREATE DATABASE employee_db;
```

## Step 3: Configure Database Connection
Edit `app.py` (around line 12) and update the database credentials:

```python
db_config = {
    'host': 'localhost',        # Your MySQL host
    'user': 'root',             # Your MySQL username
    'password': 'your_password',  # Your MySQL password (change if needed)
    'database': 'employee_db'   # Database name
}
```

**Common values:**
- host: `localhost` or `127.0.0.1`
- user: `root` (default MySQL user)
- password: (empty if you haven't set one, otherwise your MySQL password)

## Step 4: Run the Application
```
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

## Step 5: Open in Web Browser
Go to: **http://localhost:5000**

## Step 6: Test the Application

1. **Add Employee:**
   - Click "Add Employee"
   - Fill in First Name, Last Name, Pay
   - Click "Add Employee"

2. **View Employees:**
   - Go back to Home
   - See all employees in the table

3. **Edit Employee:**
   - Click "Edit" on any employee
   - Update the information
   - Click "Update Employee"

4. **Delete Employee:**
   - Click "Delete" on any employee
   - Confirm the deletion

## Troubleshooting

### "Connection refused" or MySQL error:
- Make sure MySQL is running
- Check your database credentials in app.py
- Verify the database exists

### Port 5000 already in use:
- Edit app.py, last line: `app.run(debug=True, port=5001)`
- Use a different port number

### Table not found error:
- Run `python setup_db.py` again
- Or manually create the table (see README.md)

## Next Steps

✓ The application is fully functional
✓ Database is ready for testing
✓ All CRUD operations work
✓ Both web UI and API endpoints are available

Happy testing! 🎉
