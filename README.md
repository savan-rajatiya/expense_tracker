# Expense Tracker

A command-line expense management application built with **Python** and **MySQL**.  
Track daily expenses, filter by category or month, view spending summaries, and export data to CSV — all from the terminal.

---

## Features

| #   | Option             | Description                                              |
| --- | ------------------ | -------------------------------------------------------- |
| 1   | Add Expense        | Log amount, category, optional description, and date     |
| 2   | View All Expenses  | Display every expense sorted by date (latest first)      |
| 3   | View by Category   | Filter expenses under a specific category                |
| 4   | View by Month/Year | See all expenses for any given month                     |
| 5   | Summary            | Category-wise count and total with grand total           |
| 6   | Delete Expense     | Remove a record by ID                                    |
| 7   | Export to CSV      | Save a month's expenses as `expenses_<Month>_<Year>.csv` |
| 8   | Exit               | Quit the application                                     |

---

## Tech Stack

| Layer                 | Technology               |
| --------------------- | ------------------------ |
| Language              | Python 3.12              |
| Database              | MySQL 8.0                |
| DB Connector          | `mysql-connector-python` |
| Table Formatting      | `tabulate`               |
| Environment Variables | `python-dotenv`          |

---

## Project Structure

```
Expense_Tracker/
├── db/
│   ├── __init__.py
│   └── connection.py       # DB connection + table auto-creation
├── models/
│   ├── __init__.py
│   └── expense.py          # Expense class with all CRUD + export methods
├── utils/
│   ├── __init__.py
│   └── helpers.py          # Input validation helpers
├── main.py                 # CLI menu and entry point
├── .env                    # DB credentials (not tracked)
└── .gitignore
```

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/savan-rajatiya/expense_tracker.git
cd expense_tracker
```

### 2. Install dependencies

```bash
pip install mysql-connector-python tabulate python-dotenv
```

### 3. Create a `.env` file in the project root

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=expense_tracker
```

> The database and `expenses` table are **created automatically** on first run.

### 4. Run the app

```bash
python main.py
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE expenses (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    amount      DECIMAL(10, 2)  NOT NULL,
    category    VARCHAR(50)     NOT NULL,
    description VARCHAR(255)    DEFAULT NULL,
    date        DATE            NOT NULL
);
```

---

## Categories

`Food` · `Transport` · `Shopping` · `Bills` · `Health` · `Education` · `Other`

---
