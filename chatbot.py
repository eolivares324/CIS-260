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

