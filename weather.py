from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Frankston", state="VIC", country="AU"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city},{state},{country}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")
    state = input("\nPlease enter a state name: ")
    country = input("\nPlease enter a country name: ")
    

    if not bool(city.strip()):
        city = "Frankston"

    if not bool(state.strip()):
        state = "VIC"

    if not bool(country.strip()):
        country = "AU"

    weather_data = get_current_weather(city, state, country)
    print("\n")
    pprint(weather_data)