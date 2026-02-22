# Q4: Age Calculator
# Calculates age in years, months, days, hours, minutes, and time until 100.
from datetime import datetime
def age_calculator():
    try:
        birth_year = int(input("Enter birth year: "))
        current_year = datetime.now().year
        # Calculations
        age = current_year - birth_year

        print("Age:", age)
        print("Months:", age * 12)
        print("Days:", age * 365)
        print("Hours:", age * 365 * 24)
        print("Minutes:", age * 365 * 24 * 60)
        print("Years until 100:", 100 - age)

    except:
        print("Invalid input")
# Call function
if __name__=="__main__":
    age_calculator()
