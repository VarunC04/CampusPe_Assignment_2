import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


def get_api_key():
    """Load and return Hugging Face API key."""
    load_dotenv()
    return os.getenv("HUGGINGFACE_API_KEY")


def get_hf_response(prompt, api_key):
    """Send prompt to Hugging Face and return response."""
    try:
        client = InferenceClient(api_key=api_key)

        res = client.chat_completion(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=250
        )

        return res.choices[0].message.content.strip()

    except Exception as err:
        return f"Error occurred: {err}"


def query_huggingface(prompt):
    """Query Hugging Face using the configured API key."""
    api_key = get_api_key()
    if not api_key:
        return "Error: HUGGINGFACE_API_KEY not found in environment variables."
    return get_hf_response(prompt, api_key)


def main():
    api_key = get_api_key()

    if not api_key:
        print("Error: HUGGINGFACE_API_KEY not found in environment variables.")
        return

    prompt = input("Enter your prompt for Hugging Face: ")
    print("\nThinking...")

    response = get_hf_response(prompt, api_key)

    print("\n--- Response ---")
    print(response)


if __name__ == "__main__":
    main()