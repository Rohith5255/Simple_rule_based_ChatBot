# simple_rule_based_chatbot.py

def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "weather" in user_input:
        return "Sorry, I can’t tell the weather right now, but it's sunny in my world!"
    elif "your name" in user_input:
        return "I'm FAQBot, your friendly chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that. Try asking something else!"

print("Chatbot initialized! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a nice day.")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
