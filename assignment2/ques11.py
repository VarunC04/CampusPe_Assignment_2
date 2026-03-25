# Q11: Number Pattern Printer
# Program prints 4 different patterns chosen by the user.

def number_pattern_printer():
    print("\n=== NUMBER PATTERN PRINTER ===")
    print("1. Pattern 1")
    print("2. Pattern 2")
    print("3. Pattern 3")
    print("4. Pattern 4")

    try:
        pattern_choice = int(input("Choose a pattern (1-4): "))
        height = int(input("Enter height: "))
    except ValueError:
        print("Invalid input! Enter numbers only.")
        return

    print("\n=== OUTPUT ===")

    # Pattern 1: 1, 1 2, 1 2 3, ...
    if pattern_choice == 1:
        for row in range(1, height + 1):
            for num in range(1, row + 1):
                print(num, end=" ")
            print()

    # Pattern 2: 1, 2 2, 3 3 3, ...
    elif pattern_choice == 2:
        for row in range(1, height + 1):
            for _ in range(row):
                print(row, end=" ")
            print()

    # Pattern 3: Reverse decreasing pattern
    elif pattern_choice == 3:
        for row in range(height, 0, -1):
            for num in range(row, 0, -1):
                print(num, end=" ")
            print()

    # Pattern 4: Pyramid pattern
    elif pattern_choice == 4:
        for row in range(1, height + 1):
            for num in range(1, row + 1):
                print(num, end="")
            for num in range(row - 1, 0, -1):
                print(num, end="")
            print()

    else:
        print("Invalid pattern choice!")

number_pattern_printer()