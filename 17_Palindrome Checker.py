# Q17: Palindrome Checker
# Works for both words and numbers, ignoring case.

def palindrome_checker():
    user_input = input("Enter word/number: ")

    # Convert input to lowercase for comparison
    original_text = user_input
    reversed_text = user_input[::-1]

    print("Original:", original_text)
    print("Reversed:", reversed_text)

    # Checking palindrome
    if original_text.lower() == reversed_text.lower():
        print("Result: PALINDROME")
    else:
        print("Result: NOT a palindrome")

palindrome_checker()
