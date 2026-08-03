# MySQL Database Setup Instructions

এই প্রজেক্টটি এখন **MySQL Database** ব্যবহার করতে কনফিগার করা হয়েছে।

---

## 🛠️ Step 1: `.env` ফাইলে ডাটাবেস তথ্য চেক করুন
প্রজেক্টের মূল ফোল্ডারে `.env` ফাইলে আপনার MySQL ডাটাবেসের সঠিক ইউজার ও পাসওয়ার্ড দিন:

```env
DB_ENGINE=mysql
DB_NAME=eshop_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

---

## 🗄️ Step 2: MySQL-এ ডাটাবেস তৈরি করুন
আপনার MySQL সার্ভারে (XAMPP / WAMP / MySQL Workbench / Terminal) প্রবেশ করে `eshop_db` নামের একটি ডাটাবেস তৈরি করুন:

### Terminal / Command Line:
```sql
CREATE DATABASE eshop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### phpMyAdmin (XAMPP / WAMP):
1. ব্রাউজারে `http://localhost/phpmyadmin` খুলুন।
2. **Databases** ট্যাবে গিয়ে `eshop_db` নাম দিয়ে "Create" বাটনে ক্লিক করুন।

---

## 🚀 Step 3: Migration & Data Load

### Option A: Django Command Line দিয়ে (Recommended)
```bash
# 1. টেবিলগুলো তৈরি করার জন্য:
.\venv\Scripts\python.exe manage.py migrate

# 2. ক্যাটাগরি ও প্রোডাক্ট ডাটা লোড করার জন্য:
.\venv\Scripts\python.exe manage.py loaddata initial_data.json

# 3. Admin সুপার-ইউজার তৈরির জন্য:
.\venv\Scripts\python.exe manage.py createsuperuser
```

### Option B: Direct SQL Import দিয়ে
`seed_data.sql` ফাইলটি সরাসরি আপনার phpMyAdmin বা MySQL Client-এ `eshop_db` ডাটাবেসে **Import / Run** করতে পারেন।

---

## 🌐 Step 4: Run Development Server
```bash
.\venv\Scripts\python.exe manage.py runserver
```
এরপর ব্রাউজারে [http://127.0.0.1:8000/](http://127.0.0.1:8000/) টিপলে ওয়েবসাইট চালু হয়ে যাবে!
