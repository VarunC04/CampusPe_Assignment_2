# Q16: Number Guessing Game with Difficulty Levels
# Easy:   1–50
# Medium: 1–100
# Hard:   1–1000, player gets 7 attempts.

import random

def number_guessing_game():
    best_score = None  # To track minimum number of attempts

    while True:
        print("\n=== NUMBER GUESSING GAME ===")
        print("Choose difficulty:")
        print("1. Easy   (1 - 50)")
        print("2. Medium (1 - 100)")
        print("3. Hard   (1 - 1000)")

        # Asking for difficulty with error handling
        try:
            difficulty_choice = int(input("Enter difficulty (1-3): "))
        except ValueError:
            print("Invalid input! Enter 1, 2, or 3.")
            continue

        # Setting difficulty range
        if difficulty_choice == 1:
            secret_number = random.randint(1, 50)
            max_range = 50
        elif difficulty_choice == 2:
            secret_number = random.randint(1, 100)
            max_range = 100
        elif difficulty_choice == 3:
            secret_number = random.randint(1, 1000)
            max_range = 1000
        else:
            print("Invalid choice! Choose 1, 2, or 3.")
            continue

        attempts_left = 7
        attempts_used = 0

        print(f"\nI have selected a number between 1 and {max_range}.")
        print("You have 7 attempts. Good luck!")

        # Guessing loop
        while attempts_left > 0:
            try:
                guess = int(input(f"\nEnter your guess (Attempts left {attempts_left}): "))
            except ValueError:
                print("Invalid input! Enter a valid number.")
                continue

            attempts_left -= 1
            attempts_used += 1

            # Too high or too low feedback
            if guess > secret_number:
                print("Too HIGH!")
            elif guess < secret_number:
                print("Too LOW!")
            else:
                print(f"\n Correct! You guessed the number in {attempts_used} attempts.")

                # Tracking best score
                if best_score is None or attempts_used < best_score:
                    best_score = attempts_used
                    print(" NEW BEST SCORE!")
                break

            # BONUS: Close hint
            if abs(guess - secret_number) <= 5:
                print("Hint: You're very close!")

        # If the user loses
        if attempts_left == 0 and guess != secret_number:
            print("\n You failed! The correct number was:", secret_number)

        # Asking to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

# Run the game
number_guessing_game()
