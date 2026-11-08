CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


def show_menu():
    print(f"\n{CYAN}╔══════════════════════════════╗")
    print(f"║{BOLD}      SIMPLE CALCULATOR       {RESET}{CYAN}║")
    print("╠══════════════════════════════╣")
    print("║  1. Addition        (+)      ║")
    print("║  2. Subtraction     (-)      ║")
    print("║  3. Multiplication  (×)      ║")
    print("║  4. Division        (÷)      ║")
    print("║  5. Exit                     ║")
    print(f"╚══════════════════════════════╝{RESET}")


def get_number(prompt):
    while True:
        try:
            return float(input(f"{YELLOW}{prompt}{RESET}"))
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")


def calculator():
    while True:
        show_menu()
        choice = input(f"{YELLOW}Enter your choice (1-5): {RESET}")

        if choice == '5':
            print(f"{GREEN}Goodbye!{RESET}")
            break
        if choice not in ('1', '2', '3', '4'):
            print(f"{RED}Invalid choice!{RESET}")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        else:
            if num2 == 0:
                print(f"{RED}Error! Cannot divide by zero.{RESET}")
                continue
            result = num1 / num2

        print(f"\n{GREEN}{BOLD}Result: {result}{RESET}")


calculator()