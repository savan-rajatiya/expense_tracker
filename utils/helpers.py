from datetime import datetime

def get_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print(" [!] Amount must be greater than 0.")
                continue
            return round(val, 2)
        except ValueError:
            print(" [!] Enter a valid number (e.g. 150 or 49.99).")
            
def get_choice(prompt, options):
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f" {i}. {opt}")
    while True:
        try:
            choice = int(input(" Enter number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            print(f" [!] Enter number between 1 and {len(options)}.")
        except ValueError:
            print(" [!] Enter valid number.")
            
def get_date(prompt):
    print(f"{prompt} (press Enter  for today): ", end="")
    val = input().strip()
    if not val:
        return None
    try:
        return datetime.strftime(val, "%Y-%m-%d").date()
    except ValueError:
        print(" [!] Invalid date. Using today instead.")
        return None
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" [!] Enter valid whole number.")