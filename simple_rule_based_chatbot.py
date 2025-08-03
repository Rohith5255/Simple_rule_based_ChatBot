# simple_rule_based_chatbot.py

def get_response(user_input):
    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation)).strip()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "weather" in user_input:
        return "Sorry, I can’t tell the weather right now, but it's sunny in my world!"
    elif "joke" in user_input:
        return "Why did the computer show up at work late? It had a hard drive!"
    elif "your name" in user_input:
        return "I'm FAQBot, your friendly chatbot."
    else:
        return "Sorry, I didn't understand that. Try asking something else!"

print("Chatbot initialized! Type 'bye' to exit.")

def main():
    print("Chatbot initialized! Type 'bye' to exit or 'help' for options.")

    try:
        while True:
            user_input = input("You: ")

            # Check exit condition in main loop only
            if "bye" in user_input.lower():
                print("Chatbot: Goodbye! Have a nice day.")
                break

            response = get_response(user_input)
            print("Chatbot:", response)

    except KeyboardInterrupt:
        print("\nChatbot: Session ended by user. Goodbye!")

if __name__ == "__main__":
    main()
