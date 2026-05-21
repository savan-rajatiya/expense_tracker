import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv


load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": "expense_tracker_db"
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG);
        return conn
    except Error as e:
        print(f"[DB Error] Could not Connect: {e}")
        return None
    
def setup_database():
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS expense_tracker_db")
        cursor.execute("USE expense_tracker_db")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses(
                id INT AUTO_INCREMENT PRIMARY KEY,
                amount DECIMAL(10,2) NOT NULL,
                category VARCHAR(50) NOT NULL,
                description VARCHAR(255),
                date DATE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print("[Setup] Database and Table Ready.")
    except Error as e:
        print(f"[DB Error] Setup Failed: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()