# AI API Integration Assignment

Hey there! 👋 I'm Veeresh H P, and this is my submission for the AI API Integration college assignment. 

For this project, I wanted to explore how we can connect to different AI models using Python. Instead of just sticking to one, I decided to build integrations for five different providers, including both local and cloud-based options. It was a really fun challenge to figure out how each API differs and how to bring them all together.

## What I Built

I wrote individual Python scripts for each of the following AI providers:
1. **Groq** (using LLaMA 3 8B - super fast!)
2. **Ollama** (running LLaMA 3 locally on my machine)
3. **Hugging Face** (experimenting with DialoGPT / Qwen)
4. **Google Gemini** (Gemini 2.0 Flash)
5. **Cohere** (Command R+)

To make things even easier to test, I also created a `multi_api_query.py` script. It's a unified menu where you can pick any of these providers on the fly and chat with them without having to run different files manually!

## Project Structure
Here's how I organized my code:
```text
ai-api-integration/
├── .env                  # This holds my secret API keys (ignored in git)
├── .gitignore            # Keeps my repo clean
├── cohere_example.py     # Script for Cohere
├── gemini_example.py     # Script for Google Gemini
├── groq_example.py       # Script for Groq
├── huggingface_example.py# Script for Hugging Face
├── multi_api_query.py    # The main menu to test all of them together
├── ollama_example.py     # Script for locally hosted Ollama
├── README.md             # You're reading it!
├── requirements.txt      # All the Python packages you need
└── screenshots/          # Proof that my code actually works 😄
```

## How to Set It Up

If you want to run this code on your own machine, it's pretty straightforward.

### 1. Prerequisites
- You'll need Python 3.8 or newer.
- API keys from the providers (Groq, Hugging Face, Gemini, Cohere).
- If you want to use the local Ollama option, you'll need to install Ollama and run `ollama serve` and `ollama run llama3`.

### 2. Installation
First, open a terminal in the project folder. Then, create a virtual environment to keep things clean:

```bash
python -m venv venv
```

Activate the virtual environment:
- On **Windows**: `venv\Scripts\activate`
- On **Mac/Linux**: `source venv/bin/activate`

Now, install the required packages:
```bash
pip install -r requirements.txt
```

### 3. API Keys (.env)
You'll need a `.env` file in the main folder to securely store your API keys. Make sure you don't commit this file! Here is what it should look like:

```env
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
```

## Running the Code

You have two choices here. You can either run a specific script just to test one provider:
```bash
python groq_example.py
```

Or, you can fire up my unified tool to get a nice menu of all of them:
```bash
python multi_api_query.py
```

It will ask you to pick a provider and type a prompt. The code handles the rest!

## My Experience & Challenges
The most interesting part of this assignment was seeing how each provider structures their Python SDK. Some are very straightforward (like Groq and Gemini), while others required a bit more digging into their documentation. 

I made sure not to hardcode any API keys to follow best security practices, which is why I used the `.env` approach everywhere. 

## Screenshots
*(I'll be adding the screenshots of my terminal outputs in the `screenshots/` folder for my final submission!)*
