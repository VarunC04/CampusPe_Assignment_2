# Q1: Personal Bio Card
# This program displays a formatted bio card using variables.
def personal_bio_card():
     # Using variables for each field
    name = "Varun C"
    age = 21
    course = "Python Programming"
    college = "SJBIT"
    email = "varun24@example.com"

     # Printing formatted output
    print("╔════════════════════════════════╗")
    print("║       STUDENT BIO CARD         ║")
    print("╠════════════════════════════════╣")
    print(f"║ Name    : {name:<18}   ║")
    print(f"║ Age     : {age} years{'':<10}   ║")
    print(f"║ Course  : {course:<18}   ║")
    print(f"║ College : {college:<18}   ║")
    print(f"║ Email   : {email:<18}  ║")
    print("╚════════════════════════════════╝")
    # Calling the function so it executes
if __name__ == "__main__":
    personal_bio_card()
