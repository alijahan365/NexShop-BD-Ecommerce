# NexShop - Modern E-Commerce Web Application (Django + MySQL)

A custom, full-stack E-Commerce Platform built with **Python/Django** and **MySQL Database**.

## 🌟 Key System Features
- **Product Catalog & Dynamic Categorization**: Multi-category product showcase with search and rating metrics.
- **Cart & Order Management**: Real-time shopping cart session management and order history tracking.
- **Location-Based Delivery Fee Calculation**: Automated distance calculation and ৳0.5/km delivery charge processing.
- **Digital Payment Gateways**: bKash, Nagad, Rocket, VISA/Bank Card, and Cash on Delivery options.
- **User Authentication**: Secure registration, login, and session handling.
- **MySQL Database Backend**: Powered by `PyMySQL` and Django ORM for enterprise performance.
- **Admin Management Panel**: Full Django Admin suite to manage products, categories, orders, and payment verifications.

---

## 🚀 Quick Setup Instructions

### 1. Environment & Requirements Installation
```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Database Configuration
Ensure `.env` matches your local MySQL setup:
```env
DB_NAME=eshop_db
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

### 3. Apply Database Migrations & Load Data
```bash
# Execute migrations to create MySQL tables
.\venv\Scripts\python.exe manage.py migrate

# Load initial product catalog data
.\venv\Scripts\python.exe manage.py loaddata initial_data.json
```

### 4. Create Admin Superuser Account
```bash
.\venv\Scripts\python.exe manage.py createsuperuser
```

### 5. Run Development Server
```bash
.\venv\Scripts\python.exe manage.py runserver
```
Visit application at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
