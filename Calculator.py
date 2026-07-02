def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def power(x, y):
    return x ** y

def floor_divide(x, y):
    if y == 0:
        return "Error! Floor division by zero is not allowed."
    return x // y

def modulo(x, y):
    if y == 0:
        return "Error! Modulo by zero is not allowed."
    return x % y

def calculator():
    print("--- Advanced Python Calculator ---")
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    print("6. Floor Division (//)")
    print("7. Modulo (%)")
    print("8. Exit")

    while True:
        choice = input("\nEnter choice (1-8): ").strip()

        if choice == '8':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                
            elif choice == '5':
                print(f"Result: {num1} ** {num2} = {power(num1, num2)}")
                
            elif choice == '6':
                print(f"Result: {num1} // {num2} = {floor_divide(num1, num2)}")
                
            elif choice == '7':
                print(f"Result: {num1} % {num2} = {modulo(num1, num2)}")
            
            next_calc = input("\Do another calculation? (yes/no): ").lower().strip()
            if next_calc not in ('yes', 'y'):
                print("Goodbye!")
                break
        else:
            print("Invalid Input! Please choose a valid option (1-8).")

if __name__ == "__main__":
    calculator()
else:
    print("calculator.py has been successfully imported as a module!")