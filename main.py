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
        print("║  4. Summary                  ║")
        print("║  5. Delete Expense           ║")
        print("║  6. Exit                     ║")
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
            rows = Expense.get_summary()
            Expense.display_summary(rows)
            
        elif choice == "5":
            rows = Expense.get_all()
            Expense.display(rows)
            if rows:
                exp_id = get_int("\n Enter ID to delete: ")
                Expense.delete(exp_id)
                
        elif choice == "6":
            print("\n GoodBye \n")
            break
        
        else:
            print("\n [!] Invalid option.Choose 1-6.")

if __name__ == "__main__":
    main()            