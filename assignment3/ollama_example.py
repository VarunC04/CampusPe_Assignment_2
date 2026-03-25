import requests


def get_ollama_response(prompt, model="llama3"):
    """Send prompt to local Ollama and return response."""
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        res = requests.post(url, json=payload)

        if res.status_code == 404:
            error_data = res.json()
            return (
                f"Ollama Error: {error_data.get('error', 'Endpoint not found.')}\n"
                f"Tip: Run 'ollama run {model}' in your terminal first."
            )

        res.raise_for_status()
        data = res.json()
        return data.get("response", "").strip()

    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Is it running on port 11434?"

    except Exception as err:
        return f"Error occurred: {err}"


def query_ollama(prompt):
    """Query local Ollama with the default model."""
    return get_ollama_response(prompt)


def main():
    prompt = input("Enter your prompt for Ollama: ").strip()

    if not prompt:
        print("Prompt cannot be empty.")
        return

    print("\nThinking...")

    response = get_ollama_response(prompt)

    print("\n--- Response ---")
    print(response)


if __name__ == "__main__":
    main()