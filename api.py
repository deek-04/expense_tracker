from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from mysql.mysql import engine, get_db, Base
from mysql.models import User

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Home route
@app.get("/")
def home():
    return {
        "message": "Expense Tracker API is running"
    }


# Get all expenses
@app.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):

    expenses = db.query(User).all()

    return expenses


# Add expense
@app.post("/add_expense")
def add_expense(
    amount: int,
    category: str,
    db: Session = Depends(get_db)
):

    new_expense = User(
        amount=amount,
        category=category,
        time=datetime.now()
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return {
        "message": "Expense added successfully!",
        "data": {
            "id": new_expense.id,
            "amount": new_expense.amount,
            "category": new_expense.category,
            "time": new_expense.time
        }
    }


# Total expense
@app.get("/total")
def total_expense(db: Session = Depends(get_db)):

    expenses = db.query(User).all()

    total = sum(exp.amount for exp in expenses)

    return {
        "total": total
    }


# Highest expense
@app.get("/highest_expense")
def highest_expense(db: Session = Depends(get_db)):

    expenses = db.query(User).all()

    if not expenses:
        return {
            "message": "No expenses found"
        }

    highest = max(expenses, key=lambda exp: exp.amount)

    return {
        "id": highest.id,
        "amount": highest.amount,
        "category": highest.category,
        "time": highest.time
    }


# Delete expense
@app.delete("/delete_expense/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):

    expense = db.query(User).filter(User.id == expense_id).first()

    if not expense:
        return {
            "message": "Expense not found"
        }

    db.delete(expense)
    db.commit()

    return {
        "message": "Expense deleted successfully"
    }


# Update expense
@app.put("/update_expense/{expense_id}")
def update_expense(
    expense_id: int,
    amount: int,
    category: str,
    db: Session = Depends(get_db)
):

    expense = db.query(User).filter(User.id == expense_id).first()

    if not expense:
        return {
            "message": "Expense not found"
        }

    expense.amount = amount
    expense.category = category

    db.commit()
    db.refresh(expense)

    return {
        "message": "Expense updated successfully",
        "updated_data": {
            "id": expense.id,
            "amount": expense.amount,
            "category": expense.category,
            "time": expense.time
        }
    }