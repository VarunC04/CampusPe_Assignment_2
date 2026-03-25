import os
from dotenv import load_dotenv
import cohere


def get_api_key():
    """Load and return the Cohere API key."""
    load_dotenv()
    return os.getenv("COHERE_API_KEY")


def get_cohere_response(prompt, api_key):
    """Send prompt to Cohere and return response."""
    try:
        client = cohere.Client(api_key, timeout=120)

        res = client.chat(
            model="command-r-08-2024",
            message=prompt
        )

        return res.text.strip()

    except Exception as err:
        return f"Error occurred: {err}"


def query_cohere(prompt):
    """Query Cohere using the configured API key."""
    api_key = get_api_key()
    if not api_key:
        return "Error: COHERE_API_KEY not found in environment variables."
    return get_cohere_response(prompt, api_key)


def main():
    api_key = get_api_key()

    if not api_key:
        print("Error: COHERE_API_KEY not found in environment variables.")
        return

    prompt = input("Enter your prompt for Cohere: ")
    print("\nThinking...")

    response = get_cohere_response(prompt, api_key)

    print("\n--- Response ---")
    print(response)


if __name__ == "__main__":
    main()