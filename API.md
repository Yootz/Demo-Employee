# API Documentation

## Employee Management System - RESTful API

Complete API reference for the Employee Management System.

---

## Base URL
```
http://localhost:5000
```

## Authentication
No authentication required for testing. Implement JWT or similar for production.

---

## Endpoints

### 1. GET /api/employees
**Get all employees**

```bash
curl http://localhost:5000/api/employees
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "pay": 50000.00,
    "created_at": "2026-09-16 10:30:00"
  },
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Smith",
    "pay": 55000.00,
    "created_at": "2026-09-16 10:35:00"
  }
]
```

**Query Parameters:** None

---

### 2. POST /api/employees
**Create a new employee**

```bash
curl -X POST http://localhost:5000/api/employees \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "pay": 50000
  }'
```

**Request Body:**
```json
{
  "first_name": "string (required)",
  "last_name": "string (required)",
  "pay": "number (required)"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "id": 3
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

---

### 3. PUT /api/employees/{id}
**Update an existing employee**

```bash
curl -X PUT http://localhost:5000/api/employees/1 \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Jane",
    "last_name": "Doe",
    "pay": 55000
  }'
```

**URL Parameters:**
- `id` (required) - Employee ID

**Request Body:**
```json
{
  "first_name": "string (required)",
  "last_name": "string (required)",
  "pay": "number (required)"
}
```

**Response (200 OK):**
```json
{
  "success": true
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error": "Error message"
}
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": "Employee not found"
}
```

---

### 4. DELETE /api/employees/{id}
**Delete an employee**

```bash
curl -X DELETE http://localhost:5000/api/employees/1
```

**URL Parameters:**
- `id` (required) - Employee ID

**Response (200 OK):**
```json
{
  "success": true
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error": "Error message"
}
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": "Employee not found"
}
```

---

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid parameters or data |
| 404 | Not Found - Resource doesn't exist |
| 500 | Internal Server Error - Server error |

---

## Data Types

### Employee Object
```json
{
  "id": "integer",
  "first_name": "string (100 chars max)",
  "last_name": "string (100 chars max)",
  "pay": "decimal (10.2 format)",
  "created_at": "datetime"
}
```

### Pay Format
- Decimal with 2 decimal places: `50000.00`
- Minimum value: `0.01`
- Maximum value: `99999999.99`

---

## Error Responses

All errors follow this format:

```json
{
  "success": false,
  "error": "Description of what went wrong"
}
```

### Common Errors

**Missing Required Field:**
```json
{
  "success": false,
  "error": "first_name is required"
}
```

**Invalid Data Type:**
```json
{
  "success": false,
  "error": "pay must be a number"
}
```

**Database Connection Error:**
```json
{
  "success": false,
  "error": "Connection failed"
}
```

---

## Example Usage Scenarios

### Scenario 1: Create Multiple Employees

```bash
# Employee 1
curl -X POST http://localhost:5000/api/employees \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Alice","last_name":"Johnson","pay":60000}'

# Employee 2
curl -X POST http://localhost:5000/api/employees \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Bob","last_name":"Wilson","pay":55000}'

# Employee 3
curl -X POST http://localhost:5000/api/employees \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Charlie","last_name":"Brown","pay":50000}'
```

### Scenario 2: Get All Employees and Find One

```bash
# Get all
curl http://localhost:5000/api/employees

# Find employee with ID 1 in the response
# Then update that employee
curl -X PUT http://localhost:5000/api/employees/1 \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Alicia","last_name":"Johnson","pay":65000}'
```

### Scenario 3: Delete an Employee

```bash
# Delete employee with ID 2
curl -X DELETE http://localhost:5000/api/employees/2
```

---

## Testing with Python

```python
import requests

BASE_URL = "http://localhost:5000"

# Create
response = requests.post(f"{BASE_URL}/api/employees", json={
    "first_name": "John",
    "last_name": "Doe",
    "pay": 50000
})
print(response.json())

# Read
response = requests.get(f"{BASE_URL}/api/employees")
employees = response.json()
print(employees)

# Update
response = requests.put(f"{BASE_URL}/api/employees/1", json={
    "first_name": "Jane",
    "last_name": "Doe",
    "pay": 55000
})
print(response.json())

# Delete
response = requests.delete(f"{BASE_URL}/api/employees/1")
print(response.json())
```

---

## Testing with JavaScript

```javascript
const BASE_URL = "http://localhost:5000";

// Create
fetch(`${BASE_URL}/api/employees`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        first_name: 'John',
        last_name: 'Doe',
        pay: 50000
    })
})
.then(r => r.json())
.then(data => console.log(data));

// Read
fetch(`${BASE_URL}/api/employees`)
    .then(r => r.json())
    .then(data => console.log(data));

// Update
fetch(`${BASE_URL}/api/employees/1`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        first_name: 'Jane',
        last_name: 'Doe',
        pay: 55000
    })
})
.then(r => r.json())
.then(data => console.log(data));

// Delete
fetch(`${BASE_URL}/api/employees/1`, { method: 'DELETE' })
    .then(r => r.json())
    .then(data => console.log(data));
```

---

## Rate Limiting

Currently: No rate limiting implemented

For production, consider:
- Max 100 requests per minute per IP
- Implement API key system
- Use Redis for rate limit tracking

---

## CORS

CORS is not enabled by default. To enable for frontend integration:

Add to app.py:
```python
from flask_cors import CORS
CORS(app)
```

Install: `pip install flask-cors`

---

## Security Best Practices

1. ✅ Use HTTPS in production
2. ✅ Implement authentication
3. ✅ Add input validation
4. ✅ Use rate limiting
5. ✅ Add CORS headers
6. ✅ Implement JWT tokens
7. ✅ Add request logging
8. ✅ Sanitize input data

---

## Version

- API Version: 1.0
- Last Updated: September 2026
- Status: Production Ready (with security additions)

---

For web interface documentation, see README.md
For setup instructions, see QUICKSTART.md
