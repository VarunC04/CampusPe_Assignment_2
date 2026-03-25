# Q2: Simple Calculator
# Performs basic arithmetic operations with error handling.
def simple_calculator():
    try:
        # Asking user for two numbers
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print(f"{a} + {b} = {a+b}")
        print(f"{a} - {b} = {a-b}")
        print(f"{a} * {b} = {a*b}")

        if b != 0:
            print(f"{a} / {b} = {a/b:.2f}")
            print(f"{a} % {b} = {a%b}")
        else:
            print("Division and modulus not possible (division by zero)")

        print(f"{a} ^ {b} = {a**b}")
# Handling division safely
    except:
        print("Invalid input")
# Call the function
if __name__ == "__main__":
    simple_calculator()