import requests
from dotenv import load_dotenv # type: ignore
import os
from pprint import pprint # to read json data easily, we can use pretty

load_dotenv()

def get_Current_weather():
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nEnter your city: \n")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        print("\nWeather Conditions: \n")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print(f"Error: {response.status_code}") 

if __name__ == "__main__":
    get_Current_weather()