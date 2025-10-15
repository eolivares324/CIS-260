# ==========================================================
# File: insurance_bot.py
# Purpose: Simple command-line chatbot for insurance inquiries.
# Author: Dr. Md Ali
# Description:
#   - Loads your OpenAI API key securely from an environment variable or .env file
#   - Prompts the user for an insurance-related question
#   - Uses the OpenAI Chat API to return a friendly, professional answer
# ==========================================================

# -----------------------------
# Imports
# -----------------------------
import os                    # For environment variable handling
from dotenv import load_dotenv  # For loading .env files (dev convenience)
from openai import OpenAI        # OpenAI client SDK

# -----------------------------
# Load environment variables
# -----------------------------
# If a .env file exists, this will load it into the environment.
# .env should contain a line like: OPENAI_API_KEY=sk-xxxxxxxx
load_dotenv()

# -----------------------------
# Function: get_client()
# Purpose:
#   Retrieves the OpenAI API key from the environment and initializes the client.
#   Raises an error if the key isn't found (preventing silent failure).
# -----------------------------
def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")

    # Security check: ensure the key exists before proceeding.
    if not api_key:
        raise RuntimeError(
            "ERROR: OPENAI_API_KEY not found.\n"
            "→ Please set it as an environment variable or add it to your .env file."
        )

    # Instantiate OpenAI client with the key.
    # This ensures the key isn't hardcoded anywhere in the code.
    return OpenAI(api_key=api_key)

# -----------------------------
# Function: ask_insurance_bot()
# Purpose:
#   Sends the user's question to the AI assistant with a predefined system role.
# -----------------------------
def ask_insurance_bot(user_input: str) -> str:
    client = get_client()  # Get authenticated client

    # System message sets the personality and scope of the assistant.
    system_message = {
        "role": "system",
        "content": (
            "You are an AI assistant for an insurance company. "
            "Answer questions in a friendly, professional, clear, and helpful manner. "
            "You can assist with claims, policy info, and quotes but cannot access personal data."
        ),
    }

    # User message represents the actual query
    user_message = {"role": "user", "content": user_input}

    # Send request to OpenAI’s Chat API
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # You can use 'gpt-4-turbo' or 'gpt-3.5-turbo' if preferred
        messages=[system_message, user_message],
        temperature=0.6        # Controls creativity: lower = factual, higher = creative
    )

    # Return the text response
    return response.choices[0].message.content

# -----------------------------
# Function: main()
# Purpose:
#   Entry point for running the chatbot interactively in terminal.
# -----------------------------
def main():
    print("========================================")
    print("   🏦 Your Insurance AI Helper")
    print("========================================")

    # Check if API key is loaded — print True/False (not the key itself!)
    print("OPENAI_API_KEY loaded:", bool(os.getenv("OPENAI_API_KEY")))

    try:
        # Prompt user for a question
        question = input("\nAsk the Insurance Bot: ")

        # Get AI-generated response
        reply = ask_insurance_bot(question)

        # Print the bot's reply
        print("\n🤖 Bot:", reply)

    except Exception as e:
        # Handle any runtime errors gracefully
        print("\n❌ An error occurred:", e)
        print("Make sure your .env file or environment variable is configured properly.")

# -----------------------------
# Run main() when executed directly
# -----------------------------
if __name__ == "__main__":
    main()

