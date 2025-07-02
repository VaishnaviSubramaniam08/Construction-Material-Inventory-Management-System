# Construction-Material-Inventory-Management-System

A desktop-based inventory management solution developed in Python (Tkinter) and MySQL to streamline the tracking, updating, and reporting of construction materials in real-time.

📌 Project Overview
This system is designed to help construction site managers and material handlers:
Maintain up-to-date records of construction materials
Track stock levels and receive low-quantity alerts
Generate usage reports for better material planning
Ensure accountability and reduce wastage


🛠️ Tech Stack
Frontend (GUI): Tkinter (Python Standard Library)
Backend: Python
Database: MySQL
Library: mysql-connector-python, pandas

✅ Core Features
📋 Add, Update, Delete materials
📉 Live stock level tracking
📤 Generate and export reports in CSV format
🔍 Material search and filter functionality

⚙️ Installation Guide
1. Clone the Repository
git clone https://github.com/yourusername/construction-inventory-system.git
cd construction-inventory-system

3. Install Python Dependencies
pip install mysql-connector-python pandas

5. Configure MySQL Database
CREATE DATABASE construction_inventory;
Run the SQL schema:
USE construction_inventory;

Update the database credentials in your project’s config:
# db_config.py
HOST = 'localhost'
USER = 'root'
PASSWORD = 'yourpassword'
DATABASE = 'construction_inventory'

🚀 Running the Application
python main.py


🤝 Contributions
Feel free to fork and enhance the system! PRs are welcome.

👨‍💻 Author
Vaishnavi Subramaniam
🔗 GitHub:
