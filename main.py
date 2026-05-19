from db.connection import setup_database, get_connection

if __name__ == "__main__":
    setup_database()
    conn = get_connection()
    if conn:
        print("[OK] Connection Successfull!")
        conn.close()
    else:
        print("[FAILED] Check MySQL is running and password is correct.")