from db.connection import setup_database
from models.expense import Expense, CATEGORIES
from utils.helpers import get_float, get_choice, get_date, get_int


def main():
    setup_database()
    while True:
        print("\n╔══════════════════════════════╗")
        print("║      Expense Tracker         ║")
        print("╠══════════════════════════════╣")
        print("║  1. Add Expense              ║")
        print("║  2. View All Expenses        ║")
        print("║  3. View by Category         ║")
        print("║  4. View by month/year       ║")
        print("║  5. Summary                  ║")
        print("║  6. Delete Expense           ║")
        print("║  7. Export to spreadsheet    ║")
        print("║  8. Exit                     ║")
        print("╚══════════════════════════════╝")
        
        choice = input("\n Choose an option: ").strip()
        
        if choice == "1":
            amount = get_float("\n Amount (₹): ")
            category = get_choice("\n Select category:", CATEGORIES)
            desc = input(" Description (optional): ").strip() or None
            exp_date = get_date(" Date")
            Expense.add(amount, category, desc, exp_date)
            
        elif choice == "2":
            rows = Expense.get_all()
            Expense.display(rows)
        
        elif choice == "3":
            category = get_choice("\n Select Category: ", CATEGORIES)
            rows =  Expense.get_by_category(category)
            Expense.display(rows)
            
        elif choice == "4":
            month = get_int("\n Enter Month(1-12): ", 1, 12)
            year = get_int("\n Enter Year(e.g. 2026): ", 2000,2026)
            rows = Expense.get_by_month(month, year)
            Expense.display_monthly(rows, month, year)
            
        elif choice == "5":
            rows = Expense.get_summary()
            Expense.display_summary(rows)
            
        elif choice == "6":
            rows = Expense.get_all()
            Expense.display(rows)
            if rows:
                exp_id = get_int("\n Enter ID to delete: ")
                Expense.delete(exp_id)
                
        elif choice == "7":
            month = get_int("\n Enter Month(1-12): ", 1, 12)
            year = get_int("\n Enter Year(e.g. 2026): ", 2000,2026)
            rows = Expense.get_by_month(month, year)
            if not rows:
                print("\n [!] No Expenses found for that period. Nothing exported.")
            else:
                path = Expense.export_to_csv(rows, month, year)
                print(f"\n [✓] Exported {len(rows)} record(s) -> {path}\n")
                
        elif choice == "8":
            print("\n GoodBye \n")
            break
        
        else:
            print("\n [!] Invalid option.Choose 1-8.")

if __name__ == "__main__":
    main()            