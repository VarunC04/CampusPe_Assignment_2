# Q9: Ticket Pricing System
# Calculates ticket cost based on age, day, and number of tickets.

def ticket_pricing_system():
    try:
        age = int(input("Enter age: "))
        day = input("Enter day of the week: ").strip().lower()
        number_of_tickets = int(input("Number of tickets: "))
    except ValueError:
        print("Invalid input! Provide correct values.")
        return

    if age < 3:
        base_price = 0
    elif age <= 12:
        base_price = 150
    elif age <= 59:
        base_price = 300
    else:
        base_price = 200

    # Weekend discount check
    if day in ["friday", "saturday", "sunday"]:
        discount = base_price * 0.20
    else:
        discount = 0

    price_after_discount = base_price - discount
    total_cost = price_after_discount * number_of_tickets

    print("Base price:", base_price)
    print("Discount applied:", discount)
    print("Price after discount:", price_after_discount)
    print("Total amount:", total_cost)

ticket_pricing_system()
