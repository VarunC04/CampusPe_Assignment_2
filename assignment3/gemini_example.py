import os
from dotenv import load_dotenv
from google import genai


def get_api_key():
    """Load and return Google API key."""
    load_dotenv()
    return os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")


def get_missing_key_message():
    """Return guidance when Gemini API key is missing."""
    return (
        "Error: Gemini API key not found. Set GOOGLE_API_KEY or GEMINI_API_KEY in .env.\n"
        "Example: GOOGLE_API_KEY=your_key_here"
    )


def get_gemini_response(prompt, api_key):
    """Send prompt to Gemini and return response."""
    try:
        client = genai.Client(api_key=api_key)

        res = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return res.text.strip()

    except Exception as err:
        return f"Error occurred: {err}"


def query_gemini(prompt):
    """Query Gemini using the configured API key."""
    api_key = get_api_key()
    if not api_key:
        return get_missing_key_message()
    return get_gemini_response(prompt, api_key)


def main():
    api_key = get_api_key()

    if not api_key:
        print(get_missing_key_message())
        return

    prompt = input("Enter your prompt for Google Gemini: ")
    print("\nThinking...")

    response = get_gemini_response(prompt, api_key)

    print("\n--- Response ---")
    print(response)


if __name__ == "__main__":
    main()