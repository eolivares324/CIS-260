# ==========================================================
# File: help.py
# Purpose: Simple command-line chatbot for insurance inquiries (looped version).
# Author: Emilia Olivares
# Description:
#   - Loads your OpenAI API key securely from an environment variable or .env file
#   - Repeatedly prompts the user for an insurance-related question
#   - Uses the OpenAI Chat API to return friendly, professional answers
#   - Allows user to exit easily
# ==========================================================

def chat():
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
print('Your Insurance AI Helper')
from dotenv import load_dotenv
import openai
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print("OPEN_API_KEY loaded:", bool("OPENAI_API_KEY"))
client = openai.OpenAI()

def ask_insurance_bot(user_input):
    system_message = {
        "role": "system",
        "content": (
            "You are an AI assistant for an insurance company. "
            "Answer questions friendly, professionally, clearly, and helpfully. "
            "You can assist with claims, policy info, and quotes but cannot access personal data."
        )
    }

    user_message = {"role": "user", "content": user_input}
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[system_message, user_message],
        temperature=0.6
    )

    return response.choices[0].message.content
   
if __name__ == "__main__":
    question = input("Ask the Insurance Bot: ")
    reply = ask_insurance_bot(question)
    print("Bot:", reply)

 

