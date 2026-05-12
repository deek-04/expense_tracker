# Expense Tracker API 🚀

A backend Expense Tracker project built using **FastAPI** and **MySQL** with CRUD operations and REST APIs.

## 📌 Features

* Add expenses
* View all expenses
* Calculate total expenses
* Find highest expense
* Update expenses
* Delete expenses
* MySQL database integration
* REST API testing using Swagger UI & Postman

---

# 🛠️ Tech Stack

* Python
* FastAPI
* MySQL
* SQLAlchemy
* Uvicorn
* Postman

---

# 📂 Project Structure

```text id="r1"
expense-tracker/
│
├── api.py
├── mysql/
│   ├── mysql.py
│   └── models.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash id="r2"
git clone <your-repo-link>
```

---

## Create Virtual Environment

```bash id="r3"
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash id="r4"
venv\Scripts\activate
```

---

## Install Dependencies

```bash id="r5"
pip install fastapi uvicorn sqlalchemy pymysql
```

---

# 🗄️ MySQL Setup

Create a MySQL database:

```sql id="r6"
CREATE DATABASE expense;
```

Update database credentials inside:

```text id="r7"
mysql/mysql.py
```

---

# ▶️ Run Server

```bash id="r8"
uvicorn api:app --reload
```

---

# 📖 Swagger Documentation

Open:

```text id="r9"
http://127.0.0.1:8000/docs
```

---

# 📬 API Endpoints

| Method | Endpoint             | Description         |
| ------ | -------------------- | ------------------- |
| GET    | /expenses            | Get all expenses    |
| POST   | /add_expense         | Add expense         |
| GET    | /total               | Get total expense   |
| GET    | /highest_expense     | Get highest expense |
| PUT    | /update_expense/{id} | Update expense      |
| DELETE | /delete_expense/{id} | Delete expense      |

---

# 📈 Learning Outcomes

Through this project, I learned:

* FastAPI basics
* REST API development
* CRUD operations
* MySQL database integration
* SQLAlchemy ORM
* API testing using Postman & Swagger
* Backend project structuring
<img width="1258" height="772" alt="WhatsApp Image 2026-05-10 at 10 29 57 PM (1)" src="https://github.com/user-attachments/assets/b3ac1c6f-7651-46ec-8c66-60475ceb8b4b" />
<img width="1541" height="740" alt="WhatsApp Image 2026-05-10 at 10 29 57 PM" src="https://github.com/user-attachments/assets/d0fb81f9-0518-4dbd-8bdc-5e144b1e62c1" />
<img width="1285" height="768" alt="WhatsApp Image 2026-05-10 at 10 29 58 PM" src="https://github.com/user-attachments/assets/51f22425-69cf-4f94-aaf0-35f1f8ac3d43" />


