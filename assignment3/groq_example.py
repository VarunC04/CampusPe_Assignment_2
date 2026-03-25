import os
from dotenv import load_dotenv
from groq import Groq


def get_api_key():
    """Load and return Groq API key."""
    load_dotenv()
    return os.getenv("GROQ_API_KEY")


def get_groq_response(prompt, api_key):
    """Send prompt to Groq and return response."""
    try:
        client = Groq(api_key=api_key)

        res = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
        )

        return res.choices[0].message.content.strip()

    except Exception as err:
        return f"Error occurred: {err}"


def query_groq(prompt):
    """Query Groq using the configured API key."""
    api_key = get_api_key()
    if not api_key:
        return "Error: GROQ_API_KEY not found in environment variables."
    return get_groq_response(prompt, api_key)


def main():
    api_key = get_api_key()

    if not api_key:
        print("Error: GROQ_API_KEY not found in environment variables.")
        return

    prompt = input("Enter your prompt for Groq: ")
    print("\nThinking...")

    response = get_groq_response(prompt, api_key)

    print("\n--- Response ---")
    print(response)


if __name__ == "__main__":
    main()