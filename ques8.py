# Q8: Leap Year Checker
# Uses the leap year rules and explains the reason.

def leap_year_checker():
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("Invalid input! Enter a valid year.")
        return

    # Applying leap year rules
    if year % 4 != 0:
        print(year, "is NOT a leap year — not divisible by 4.")
    elif year % 100 != 0:
        print(year, "IS a leap year — divisible by 4 but not by 100.")
    elif year % 400 == 0:
        print(year, "IS a leap year — divisible by 400.")
    else:
        print(year, "is NOT a leap year — divisible by 100 but not by 400.")

leap_year_checker()