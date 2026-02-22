# Q15: Prime Number Checker
# Includes:
# Part 1: Check if a single number is prime
# Part 2: Find all prime numbers in a range

def is_prime(num):
    # Handling edge cases first
    if num < 2:
        return False
    if num == 2:
        return True

    # Checking divisibility
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_checker():
    # ---- PART 1: Single Number ----
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input!")
        return

    if is_prime(number):
        print(number, "is a PRIME number")
    else:
        print(number, "is NOT a prime number")

    # ---- PART 2: Range ----
    try:
        start_range = int(input("Enter start range: "))
        end_range = int(input("Enter end range: "))
    except ValueError:
        print("Invalid input!")
        return

    prime_list = [n for n in range(start_range, end_range + 1) if is_prime(n)]
    print("Prime numbers:", ", ".join(map(str, prime_list)))

prime_checker()
