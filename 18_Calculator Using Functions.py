# Q18: Calculator Using Functions
# Includes menu-driven program calling arithmetic functions.

import math

# Basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error (division by zero)"

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    try:
        if a < 0:
            return "Error (square root of negative number)"
        return math.sqrt(a)
    except:
        return "Invalid input!"

def percentage(a, b):
    # a% of b
    return (a / 100) * b


def calculator():
    while True:
        print("\n=== ADVANCED CALCULATOR MENU ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 9:
            print("Exiting calculator...")
            break

        # Functions requiring 2 inputs
        if choice in [1, 2, 3, 4, 5, 6, 8]:
            try:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input!")
                continue

        # Square Root needs 1 input
        if choice == 7:
            try:
                number = float(input("Enter number: "))
            except ValueError:
                print("Invalid input!")
                continue

        # Calling correct functions
        if choice == 1:
            print("Result:", add(first_number, second_number))
        elif choice == 2:
            print("Result:", subtract(first_number, second_number))
        elif choice == 3:
            print("Result:", multiply(first_number, second_number))
        elif choice == 4:
            print("Result:", divide(first_number, second_number))
        elif choice == 5:
            print("Result:", modulus(first_number, second_number))
        elif choice == 6:
            print("Result:", power(first_number, second_number))
        elif choice == 7:
            print("Result:", square_root(number))
        elif choice == 8:
            print(f"{first_number}% of {second_number} =", percentage(first_number, second_number))
        else:
            print("Invalid choice!")

# Run the calculator
calculator()
