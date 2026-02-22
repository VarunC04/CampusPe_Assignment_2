# Q14: Factorial Calculator
# Handles 0, negative numbers, and step-by-step factorial explanation.

def factorial_calculator():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input!")
        return

    if number < 0:
        print("Factorial of negative numbers is not defined.")
        return

    # Calculating factorial step-by-step
    factorial_value = 1
    steps = ""

    for i in range(number, 0, -1):
        factorial_value *= i
        steps += f"{i} × " if i > 1 else f"{i}"

    print(f"{number}! = {steps} = {factorial_value}")

factorial_calculator()
