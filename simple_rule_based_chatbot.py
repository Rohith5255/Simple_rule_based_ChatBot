# simple_rule_based_chatbot.py
import string
import requests
API_KEY = '905f2fc535322f13ea4629ab678d55b9'
def get_response(user_input):
    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation)).strip()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "joke" in user_input:
        return "Why did the computer show up at work late? It had a hard drive!"
    elif "your name" in user_input:
        return "I'm FAQBot, your friendly chatbot."
    else:
        return "Sorry, I didn't understand that. Try asking something else!"

print("Chatbot initialized! Type 'bye' to exit.")

def fetch_weather(country, state, city, api_key):
    # Query OpenWeatherMap. Not all regions have 'state' parameter in OWM. We'll use city and country.
    # For US cities: q=city,state,country (ISO codes). For most others: q=city,country code.
    location = f"{city},{state},{country}" if state else f"{city},{country}"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        return f"Weather in {city}, {state}, {country}: {weather.capitalize()}, Temp: {temp}°C, Feels like: {feels_like}°C."
    else:
        return f"Sorry, I couldn't retrieve the weather for {city}, {state}, {country}. Please check the city/state/country names."
    
def main():
    print("Chatbot initialized! Type 'bye' to exit or 'help' for options.")

    try:
        while True:
            user_input = input("You: ")

            # Check exit condition in main loop only
            if "bye" in user_input.lower():
                print("Chatbot: Goodbye! Have a nice day.")
                break

            if "weather" in user_input.lower():
                print("Chatbot: Sure, to get the weather, please provide the details.")
                country = input("Country (2-letter code, e.g. IN for India, US for United States): ")
                state = input("State (optional, press Enter to skip): ")
                city = input("City: ")
                print("Chatbot: Fetching weather information...")
                weather_response = fetch_weather(country.strip(), state.strip(), city.strip(), API_KEY)
                print("Chatbot:", weather_response)
            else:
                response = get_response(user_input)
                print("Chatbot:", response)
    except KeyboardInterrupt:
        print("\nChatbot: Session ended by user. Goodbye!")

if __name__ == "__main__":
    main()
