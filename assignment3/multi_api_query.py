import sys
from groq_example import query_groq
from ollama_example import query_ollama
from huggingface_example import query_huggingface
from gemini_example import query_gemini
from cohere_example import query_cohere


PROVIDERS = {
    "1": ("Groq", query_groq),
    "2": ("Ollama (Local)", query_ollama),
    "3": ("Hugging Face", query_huggingface),
    "4": ("Google Gemini", query_gemini),
    "5": ("Cohere", query_cohere),
}


def display_menu():
    print("=== AI API Integration ===")
    for key, (name, _) in PROVIDERS.items():
        print(f"{key}. {name}")
    print("0. Exit")


def get_user_choice():
    return input("\nSelect a provider (0-5): ").strip()


def handle_selection(choice):
    if choice == "0":
        print("Exiting...")
        sys.exit(0)

    if choice not in PROVIDERS:
        print("Invalid selection. Please try again.")
        return

    provider_name, query_func = PROVIDERS[choice]

    print(f"\n--- Selected {provider_name} ---")
    prompt = input("Enter your prompt: ").strip()

    if not prompt:
        print("Prompt cannot be empty.")
        return

    print(f"\nThinking using {provider_name}...")
    result = query_func(prompt)

    print("\n--- Response ---")
    print(result)


def main():
    display_menu()
    choice = get_user_choice()
    handle_selection(choice)


if __name__ == "__main__":
    try:
        while True:
            main()
            print("\n" + "=" * 40 + "\n")
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)