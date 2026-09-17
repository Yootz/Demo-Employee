#!/bin/bash
# Employee Management System - Startup Script
# Run this to quickly start the application

echo ""
echo "============================================================"
echo "  Employee Management System - Startup"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7+ from python.org"
    exit 1
fi

echo "[1] Installing required packages..."
echo ""
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install packages"
    exit 1
fi

# echo ""
# echo "[2] Setting up database..."
# python3 setup_db.py

# if [ $? -ne 0 ]; then
#     echo "ERROR: Failed to setup database"
#     echo "Make sure MySQL is installed and running"
#     exit 1
# fi

echo ""
echo "============================================================"
echo "  Starting Employee Management System..."
echo "============================================================"
echo ""
echo "  Web Interface: http://localhost:5000"
echo "  API Endpoints available at /api/employees"
echo ""
echo "  Press CTRL+C to stop the server"
echo ""
echo "============================================================"
echo ""

python3 app.py
