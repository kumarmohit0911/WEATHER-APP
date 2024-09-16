import requests

API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    try:
        # Construct URL to fetch weather data
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Check if the city is found
        if data['cod'] != 200:
            print("City not found!")
            return

        # Extracting relevant weather information
        weather_data = {
            "city": data['name'],
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }

        # Display the weather information
        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Weather: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
