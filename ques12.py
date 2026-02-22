# Q12: Multiplication Table Generator

def multiplication_table():
    try:
        base_number = int(input("Enter number: "))
        end_range = int(input("Enter range (end): "))
    except ValueError:
        print("Invalid input! Enter numbers only.")
        return

    print(f"\nMultiplication Table of {base_number}")
    for multiplier in range(1, end_range + 1):
        print(f"{base_number} x {multiplier} = {base_number * multiplier}")

multiplication_table()