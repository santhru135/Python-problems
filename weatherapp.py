import requests

# Your API key
API_KEY = "bd5e378503939ddaee76f12ad7a97608"

# Ask the user for a city name
city = input("Enter city name: ")

# API endpoint
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Display weather info
if response.status_code == 200:
    print(f"\nWeather in {city.title()}: {data['weather'][0]['description'].title()}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels Like: {data['main']['feels_like']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    print("\nError:", data.get("message", "Unable to fetch weather details"))
