# Q3: String Manipulator
# This program analyzes a sentence in multiple ways.

def string_manipulator():
    user_sentence = input("Enter a sentence: ")

    # Basic operations on the string
    characters_with_spaces = len(user_sentence)
    characters_without_spaces = len(user_sentence.replace(" ", ""))
    words_list = user_sentence.split()
    total_words = len(words_list)

    # Handling empty string case
    if total_words == 0:
        print("You entered an empty sentence.")
        return

    # Extracting first and last words safely
    first_word = words_list[0]
    last_word = words_list[-1]

    # Reversing the sentence
    reversed_sentence = " ".join(word[::-1] for word in words_list[::-1])

    # Displaying results
    print("Original:", user_sentence)
    print("Characters (with spaces):", characters_with_spaces)
    print("Characters (without spaces):", characters_without_spaces)
    print("Words:", total_words)
    print("UPPERCASE:", user_sentence.upper())
    print("lowercase:", user_sentence.lower())
    print("Title Case:", user_sentence.title())
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Reversed:", reversed_sentence)

# Call the function
string_manipulator()
