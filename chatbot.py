# ==========================================================
# File: help.py
# Purpose: Command-line chatbot for insurance professionals
# Author: Emilia Olivares (Enhanced Version)
# Description:
#   - Securely loads your OpenAI API key
#   - Provides friendly, professional insurance assistance
#   - Maintains conversation context
#   - Offers quick commands for common insurance topics
#   - Logs all chats for review or compliance
#   - Customizes tone for different insurance roles
# ==========================================================

# -----------------------------
# Imports
# -----------------------------
import os                      # For environment variable handling
import datetime                 # For timestamped logging
from dotenv import load_dotenv  # For loading .env files (dev convenience)
from openai import OpenAI       # OpenAI client SDK

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
#   Sends the user's question to the AI assistant with conversation memory and role context.
# -----------------------------
def ask_insurance_bot(user_input: str, conversation_history: list, role: str) -> str:
    client = get_client() # Get authenticated client

    # System message sets the personality and scope of the assistant.
    system_message = {
        "role": "system",
        "content": (
             "You are an AI assistant for an insurance company. "
             "You are currently assisting an insurance agent. "
             "Answer questions in a friendly, professional, clear, and helpful manner. "
            "Provide accurate and ethical information about claims, policy details, and quotes, but never access or request personal data. "
            "Maintain context across multiple messages in this conversation."
        ),
    }

    # Combine prior conversation with new question
    messages = [system_message] + conversation_history + [{"role": "user", "content": user_input}]

    # Send request to OpenAI's Chat API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.6,
    )

    # Extract the text reply
    reply = response.choices[0].message.content

    # Append to conversation history
    conversation_history.append({"role": "user", "content": user_input})
    conversation_history.append({"role": "assistant", "content": reply})

    return reply


# -----------------------------
# Function: log_interaction()
# Purpose:
#   Logs user and bot messages to a file with timestamps.
# -----------------------------
def log_interaction(user_input: str, bot_reply: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] User: {user_input}\n")
        log.write(f"[{timestamp}] Bot: {bot_reply}\n\n")


# -----------------------------
# Function: main()
# Purpose:
#   Entry point for running the chatbot interactively in terminal (looped version).
# -----------------------------
def main():
    print("========================================")
    print("       Your Insurance AI Helper")
    print("========================================")
    
    # Check if API key is loaded — print True/False (not the key itself!)

    print("OPENAI_API_KEY loaded:", bool(os.getenv("OPENAI_API_KEY")))

    # Role customization for tone and context
    role = input("\nEnter your role (e.g., 'claims adjuster', 'agent', 'customer support'): ").strip() or "insurance professional"
    print("Welcome! Type 'help' for quick commands or 'exit' to quit.\n")

    # Initialize conversation memory
    conversation_history = []

    # Predefined quick commands for convenience
    QUICK_COMMANDS = {
        "help": (
            "Available quick commands:\n"
            "  help       - Show this list\n"
            "  policies   - List common policy types\n"
            "  claims     - Outline standard claim steps\n"
            "  coverage   - Summarize standard coverage\n"
            "  exit/quit  - End the session"
        ),
        "policies": (
            "Common policy types include:\n"
            "- Auto Insurance\n"
            "- Homeowners Insurance\n"
            "- Life Insurance\n"
            "- Health Insurance\n"
            "- Commercial Property Insurance"
        ),
        "claims": (
            "Typical claim process:\n"
            "1. Report the incident promptly.\n"
            "2. Provide necessary documentation (photos, police reports, etc.).\n"
            "3. An adjuster reviews and investigates the claim.\n"
            "4. Receive settlement or explanation of coverage."
        ),
        "coverage": (
            "Standard coverage often includes:\n"
            "- Liability protection\n"
            "- Property damage coverage\n"
            "- Personal injury protection\n"
            "- Optional add-ons such as roadside assistance or rental reimbursement."
        ),
    }

    try:
        # Continuous conversation loop
        while True:
            # Prompt user for input
            question = input("\nAsk the Insurance Bot (or type 'exit' to quit): ").strip()

            # Exit condition
            if question.lower() in {"exit", "quit"}:
                print("\nThank you for using the Insurance AI Helper. Goodbye!")
                break

            # Handle quick commands
            if question.lower() in QUICK_COMMANDS:
                print("\nBot:", QUICK_COMMANDS[question.lower()])
                continue

            # Skip empty input
            if not question:
                print("Please enter a question or type 'exit' to quit.")
                continue

            # Generate and display AI response
            reply = ask_insurance_bot(question, conversation_history, role)
            print("\nBot:", reply)

            # Log each exchange for record-keeping
            log_interaction(question, reply)

    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        print("\n\nSession terminated by user. Goodbye!")

    except Exception as e:
        # Friendly and graceful error handling
        print("\nAn error occurred:", e)
        if "api_key" in str(e).lower():
            print("→ It seems your OpenAI API key is missing or invalid.")
        elif "rate_limit" in str(e).lower():
            print("→ You may have hit a rate limit. Try again in a few moments.")
        else:
            print(f"→ Details: {e}")
        print("\nMake sure your .env file or environment variable is configured properly.")


# -----------------------------
# Run main() when executed directly
# -----------------------------
if __name__ == "__main__":
    main()
