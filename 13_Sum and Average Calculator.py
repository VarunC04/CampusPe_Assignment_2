# Q13: Sum and Average Calculator
# Calculates sum, average, max, and min using input loop.
def sum_average_statistics():
    try:
        total_count = int(input("How many numbers? "))
    except ValueError:
        print("Invalid input!")
        return

    if total_count <= 0:
        print("Count must be greater than 0.")
        return

    numbers = []

    # Collect numbers
    for i in range(1, total_count + 1):
        try:
            value = float(input(f"Enter number {i}: "))
            numbers.append(value)
        except ValueError:
            print("Invalid number!")
            return

    # Basic calculations
    total_sum = sum(numbers)
    average = total_sum / total_count
    maximum_value = max(numbers)
    minimum_value = min(numbers)

    sorted_numbers = sorted(numbers)
    mid = total_count // 2

    if total_count % 2 == 1:
        median_value = sorted_numbers[mid]
    else:
        median_value = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    highest_frequency = max(frequency.values())
    mode_values = [num for num, count in frequency.items() if count == highest_frequency]

    print("\n=== STATISTICS ===")
    print("Numbers:", numbers)
    print("Sum:", total_sum)
    print("Average:", average)
    print("Maximum:", maximum_value)
    print("Minimum:", minimum_value)
    print("Median:", median_value)

    # If all numbers appear once → no real mode
    if len(mode_values) == len(numbers):
        print("Mode: No mode (all numbers are unique)")
    else:
        print("Mode:", mode_values)

# Run the program
sum_average_statistics()
