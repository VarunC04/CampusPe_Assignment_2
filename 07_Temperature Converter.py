# Q7: Temperature Converter
# Menu-driven program for temperature conversion.

def temperature_converter():
    while True:
        print("\n===== TEMPERATURE CONVERTER =====")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        try:
            user_choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input! Enter a number 1–7.")
            continue

        if user_choice == 7:
            print("Exiting converter...")
            break

        try:
            temperature_value = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid temperature entered!")
            continue

        # Performing conversions based on menu choice
        if user_choice == 1:
            print("Result:", (temperature_value * 9/5) + 32, "°F")
        elif user_choice == 2:
            print("Result:", (temperature_value - 32) * 5/9, "°C")
        elif user_choice == 3:
            print("Result:", temperature_value + 273.15, "K")
        elif user_choice == 4:
            print("Result:", temperature_value - 273.15, "°C")
        elif user_choice == 5:
            print("Result:", (temperature_value - 32) * 5/9 + 273.15, "K")
        elif user_choice == 6:
            print("Result:", (temperature_value - 273.15) * 9/5 + 32, "°F")
        else:
            print("Invalid choice! Please pick between 1 and 7.")

temperature_converter()
