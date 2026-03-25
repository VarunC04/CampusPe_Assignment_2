# Q19: Text Analysis Functions

def count_words(text):
    return len(text.split())

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def count_consonants(text):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in letters and char not in vowels)

def reverse_text(text):
    return " ".join(word[::-1] for word in text.split()[::-1])

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))

    lw = longest_word(text)
    print(f"Longest word: {lw} ({len(lw)} letters)")

    freq = word_frequency(text)
    print("Word Frequency:")
    for word, count in freq.items():
        print(f"{word}: {count}")

# User input
user_text = input("Enter text: ")
analyze_text(user_text)