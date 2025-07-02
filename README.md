
🧱 Construction Material Inventory Management System
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
2. Install Python Dependencies

pip install mysql-connector-python pandas
3. Configure MySQL Database
Create database:


CREATE DATABASE construction_inventory;
Run the SQL schema:


USE construction_inventory;
SOURCE schema.sql;
Update the database credentials in your project’s config:


# db_config.py
HOST = 'localhost'
USER = 'root'
PASSWORD = 'yourpassword'
DATABASE = 'construction_inventory'
🚀 Running the Application

python main.py


📸 Screenshots
![Dahboard Page](https://github.com/user-attachments/assets/cc4a8cdd-08df-492e-bd08-4bba8e2fd89e)

![Employee Dahboard](https://github.com/user-attachments/assets/2366aa9e-0190-4164-952c-2da0a05664ed)

![Supplier Dashboard](https://github.com/user-attachments/assets/becdc54e-3433-4960-a881-aa32a92a87c2)

![Category Dahboard](https://github.com/user-attachments/assets/6e20e79b-de75-41ed-a0a8-c12d214e3d74)

![Sales Page](https://github.com/user-attachments/assets/3d40c320-951b-4961-bb74-eaa6f61e98d6)



🤝 Contributions
Feel free to fork and enhance the system! PRs are welcome.

🔗 GitHub: https://github.com/VaishnaviSubramaniam08

