# Weather App: Create a command-line application that allows users to enter a city name and displays the current weather condition
# using an API like OpenWeatherMap. You can use Python's requests module to make HTTP requests to the API and parse the response data.

import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def display_weather(city, weather):
    if weather is not None:
        temperature = weather["main"]["temp"]
        description = weather["weather"][0]["description"]
        print(f"Current weather in {city}: {description}, {temperature:.1f}°C")  
    else:
        print(f"Could not get weather data for {city}")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    api_key = "f6dc6a5f4369cd6eb12b8acb7cb49c16"
    weather = get_weather(city, api_key)
    display_weather(city, weather)
