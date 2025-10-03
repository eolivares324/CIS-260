## Please review this code.

import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "how are you": ["I'm doing well, thanks!", "Great! How about you?"]
}

def preprocess(text):
    """Simple preprocessing (lowercasing)."""
    return text.lower()

def get_response(user_input):
    """Return chatbot response based on user input."""
    user_input = preprocess(user_input)
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure I understand. Can you rephrase?"

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



