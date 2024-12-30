import requests
from .personalization import get_weather_unit

def get_weather(city):
    api_key = "bcea0ada9717b43705d8169368f41267"  # Replace with your OpenWeather API key
    unit = get_weather_unit().lower()
    
    
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}"
    
    #At the time of Sending Request check if City is not entered - Error fetching weather data: 400 Client Error: Bad Request for url: http://api.openweathermap.org/data/2.5/weather?q=&units=celsius&appid=bcea0ada9717b43705d8169368f41267
    if city == None:
        return f"City {city} not found."

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Will raise an exception for bad responses
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            unit_symbol = "°C" if unit == "metric" else "°F"
            return f"The temperature in {city} is {temperature:.2f}{unit_symbol}."
        else:
            return f"City {city} not found."
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
