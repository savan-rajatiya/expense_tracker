from db.connection import get_connection
from tabulate import tabulate
from datetime import date

CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Health", "Education", "Other"]

class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        
    # ─── CREATE ───────────────────────────────────────────
    
    def add(amount, category, description, expense_date=None):
        conn = get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO expenses(amount, category, description, date)
                VALUES (%s, %s, %s, %s)
            """, (amount, category, description, expense_date or date.today()))
            conn.commit()
            print(f"\n[✓] Expense of ₹{amount:.2f} added under '{category}'.")
            return True
        except Exception as e:
            print(f"[Error] Could not add expense: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
     
    # ─── READ ALL ─────────────────────────────────────────
    
    def get_all():
        conn = get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, amount, category, description, date
                FROM expenses
                ORDER BY date DESC
            """)
            return cursor.fetchall()
        
        except Exception as e:
            print(f"[Error] Could not fetch expenses: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
        
    # ─── READ BY CATEGORY ─────────────────────────────────
    
    def get_by_category(category):
        conn = get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, amount, category, description, date
                FROM expenses
                WHERE category = %s
                ORDER BY date DESC
            """,(category,))
            return cursor.fetchall()
        except Exception as e:
            print(f"[Error] Could not fetch: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    # ─── DELETE ───────────────────────────────────────────
    
    def delete(expense_id):
        conn = get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
            if cursor.rowcount == 0:
                print(f"[!] No expense found with ID {expense_id}.")
                return False
            conn.commit()
            print(f"[✓] Expense #{expense_id} deleted.")
            return True
        except Exception as e:
            print(f"[Error] Could not delte: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
            
    # ─── SUMMARY ──────────────────────────────────────────
     
    def get_summary():
        conn =get_connection()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT category, COUNT(*) as count, SUM(amount) as total
                FROM expenses
                GROUP BY category
                ORDER BY total DESC
            """)
            return cursor.fetchall()
        except Exception as e:
            print(f"[Error] Could not featch summary: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    # ─── DISPLAY HELPERS ──────────────────────────────────
    
    def display(rows):
        if not rows:
            print("\n No expenses found.")
            return
        headers = ["ID", "Amount (₹)", "Category", "Description", "Date"]
        formatted = [(r[0], f"{r[1]:.2f}", r[2], r[3] or "-", r[4])for r in rows]
        print("\n"+tabulate(formatted, headers = headers, tablefmt = "rounded_outline"))
        
    def display_summary(rows):
        if not rows:
            print("\n No data yet.")
            return
        headers = ["Category", "Count", "Total (₹)"]
        formatted = [(r[0], r[1], f"{r[2]:.2f}") for r in rows]
        print("\n" + tabulate(formatted, headers = headers, tablefmt = "rounded_outline"))
        total = sum(r[2] for r in rows)
        print(f" {'-'*34}")
        print(f"Grand Total: ₹{total:.2f}\n")