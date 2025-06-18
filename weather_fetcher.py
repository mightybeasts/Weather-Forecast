# weather_fetcher.py
import requests
import pandas as pd
from config import API_KEY, BASE_URL

def fetch_weather_data(city, days=1):
    params = {
        "key": API_KEY,
        "q": city,
        "days": days,
        "aqi": "no",
        "alerts": "no"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        return None, f"Error: {response.status_code}"
    
    data = response.json()

    # Extract current conditions
    current = {
        "city": data['location']['name'],
        "country": data['location']['country'],
        "temp_c": data['current']['temp_c'],
        "condition": data['current']['condition']['text'],
        "humidity": data['current']['humidity'],
        "wind_kph": data['current']['wind_kph'],
        "is_day": data['current']['is_day'],
        "localtime": data['location']['localtime']
    }

    # Extract hourly forecast
    hours = data['forecast']['forecastday'][0]['hour']
    forecast_df = pd.DataFrame([{
        "time": hour["time"],
        "temperature": hour["temp_c"],
        "condition": hour["condition"]["text"]
    } for hour in hours])

    lat = data['location']['lat']
    lon = data['location']['lon']

    return {"current": current, "forecast_df": forecast_df, "lat": lat, "lon": lon}, None
