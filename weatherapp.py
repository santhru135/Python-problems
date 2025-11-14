import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"\nWeather in {city.title()}: {data['weather'][0]['description'].title()}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels Like: {data['main']['feels_like']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    print("\nError:", data.get("message", "Unable to fetch weather details"))
