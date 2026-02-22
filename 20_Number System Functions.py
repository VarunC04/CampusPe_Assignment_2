# Q20: Number System Functions
# Includes factorial, prime check, Fibonacci, sum of digits, reverse number,
# Armstrong check, GCD, LCM, perfect number check, and a main menu.

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d)**power for d in digits) == n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci Number")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 10:
            print("Exiting Number System Menu...")
            break

        try:
            if choice in [1, 2, 3, 4, 5, 6, 9]:
                n = int(input("Enter a number: "))
            if choice in [7, 8]:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            print("Factorial:", factorial(n))
        elif choice == 2:
            print("Prime:", is_prime(n))
        elif choice == 3:
            print("Fibonacci:", fibonacci(n))
        elif choice == 4:
            print("Sum of digits:", sum_of_digits(n))
        elif choice == 5:
            print("Reversed number:", reverse_number(n))
        elif choice == 6:
            print("Armstrong:", is_armstrong(n))
        elif choice == 7:
            print("GCD:", gcd(a, b))
        elif choice == 8:
            print("LCM:", lcm(a, b))
        elif choice == 9:
            print("Perfect Number:", is_perfect_number(n))
        else:
            print("Invalid choice.")

math_menu()
