# Q5: Bill Splitter
# Splits a restaurant bill among people with tax and tip calculations.
def bill_splitter():
    try:
        bill = float(input("Enter total bill: "))
        people = int(input("Number of people: "))
        tax_percent = float(input("Tax percentage: "))
        tip_percent = float(input("Tip percentage: "))

        # Handling invalid people count
        if people <= 0:
            print("Number of people must be greater than zero.")
            return

        tax = bill * tax_percent / 100
        after_tax = bill + tax

        tip = after_tax * tip_percent / 100
        total = after_tax + tip

        per_person = total / people

        print("\n=== BILL BREAKDOWN ===")
        print("Subtotal:", bill)
        print("Tax:", tax)
        print("After tax:", after_tax)
        print("Tip:", tip)
        print("Total:", total)
        print("Per person:", per_person)

    except:
        print("Invalid input")
# Call function
if __name__=="__main__":
    bill_splitter()
