import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve API key securely
API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITY = "Nairobi"

# Check whether the API key exists
if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("City:", data["name"])
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", weather)

    # Plot temperature
    plt.bar(["Temperature"], [temperature])
    plt.title(f"Current Temperature in {data['name']}")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.show()

except requests.exceptions.RequestException as error:
    print("Weather API request failed:", error)

except (KeyError, IndexError, ValueError):
    print("Unexpected response received from the weather API.")
